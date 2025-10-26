# core/views.py
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
import random
import re
import requests  # 런팟 API 호출을 위한 HTTP 라이브러리
import os  # 환경변수 사용을 위한 os 모듈

# ===== 서버 유효성 검사 규칙 =====
NICKNAME_RE = re.compile(r'^[A-Za-z0-9가-힣]{2,20}$')
PASSWORD_RE = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{10,}$')


def index(request):
    return render(request, 'pages/index.html')


# =========================
# AJAX APIs
# =========================
def nickname_check(request):
    username = (request.GET.get('username') or '').strip()
    if not NICKNAME_RE.match(username):
        return JsonResponse({'ok': False, 'reason': '닉네임은 2~20자 한글/영문/숫자만 가능'})
    if User.objects.filter(username=username).exists():
        return JsonResponse({'ok': False, 'reason': '이미 사용 중인 닉네임'})
    return JsonResponse({'ok': True})


def send_email_code(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'reason': 'POST만 허용'}, status=405)

    email = (request.POST.get('email') or '').strip().lower()
    if not email or '@' not in email or '.' not in email:
        return JsonResponse({'ok': False, 'reason': '이메일 형식이 올바르지 않습니다.'})

    # ★ 0) DB 중복 이메일은 처음부터 차단
    from django.contrib.auth.models import User
    if User.objects.filter(email__iexact=email).exists():
        return JsonResponse({
            'ok': False,
            'blocked': 'registered',
            'reason': '이미 인증된 이메일입니다. (가입된 이메일)'
        })

    now_ts = int(timezone.now().timestamp())
    data = request.session.get('email_verify')

    # 1) 동일 이메일 + 이미 인증 완료 → 차단
    if data and data.get('email') == email and data.get('verified'):
        return JsonResponse({
            'ok': False,
            'blocked': 'verified',
            'reason': '이미 인증 완료된 이메일입니다.'
        })

    # 2) 동일 이메일 + 유효시간 내 재요청 → 남은 초 안내 후 차단
    if data and data.get('email') == email and isinstance(data.get('expires_ts'), int):
        remain = data['expires_ts'] - now_ts
        if remain > 0:
            return JsonResponse({
                'ok': False,
                'blocked': 'cooldown',
                'remain': remain,
                'reason': f'이미 전송됨. {remain}초 뒤 다시 시도하세요.'
            })

    # 3) 새 코드 발급
    code = f"{random.randint(100000, 999999)}"
    expires_ts = int((timezone.now() + timedelta(minutes=5)).timestamp())
    request.session['email_verify'] = {
        'email': email,
        'code': code,
        'expires_ts': expires_ts,
        'verified': False,
    }

    send_mail(
        subject='[베이비가이드] 이메일 인증 코드',
        message=f'인증 코드: {code} (5분 내 유효)',
        from_email=None,
        recipient_list=[email],
        fail_silently=True,
    )
    return JsonResponse({'ok': True, 'message': '인증번호가 발송되었습니다.', 'expires_in': 300})

def verify_email_code(request):
    """입력한 6자리 코드 검증."""
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'reason': 'POST만 허용'}, status=405)

    email = (request.POST.get('email') or '').strip().lower()
    code = (request.POST.get('code') or '').strip()

    data = request.session.get('email_verify')
    if not data:
        return JsonResponse({'ok': False, 'reason': '인증 요청을 먼저 해주세요.'})
    if data.get('email') != email:
        return JsonResponse({'ok': False, 'reason': '요청한 이메일과 다릅니다.'})

    now_ts = int(timezone.now().timestamp())
    expires_ts = data.get('expires_ts')
    if not isinstance(expires_ts, int):
        return JsonResponse({'ok': False, 'reason': '세션 정보가 올바르지 않습니다. 다시 요청하세요.'})
    if now_ts > expires_ts:
        return JsonResponse({'ok': False, 'reason': '인증 유효시간(5분) 만료. 재요청하세요.'})

    if data.get('code') != code:
        return JsonResponse({'ok': False, 'reason': '인증번호가 일치하지 않습니다.'})

    data['verified'] = True
    request.session['email_verify'] = data
    return JsonResponse({'ok': True, 'message': '이메일 인증이 완료되었습니다.'})


# =========================
# 페이지 뷰
# =========================
def signup_view(request):
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        email = (request.POST.get('email') or '').strip().lower()
        password = request.POST.get('password') or ''
        password2 = request.POST.get('password2') or ''

        # 1) 서버 유효성 검사
        if not NICKNAME_RE.match(username):
            return render(request, 'pages/join.html', {'error': '닉네임은 2~20자 한글/영문/숫자만 가능합니다.'})
        if User.objects.filter(username=username).exists():
            return render(request, 'pages/join.html', {'error': '이미 존재하는 닉네임입니다.'})
        if '@' not in email or '.' not in email:
            return render(request, 'pages/join.html', {'error': '이메일 형식이 올바르지 않습니다.'})
        # 이메일 중복 차단(대소문자 무시)
        if User.objects.filter(email__iexact=email).exists():
            return render(request, 'pages/join.html', {'error': '이미 가입된 이메일입니다.'})
        if password != password2:
            return render(request, 'pages/join.html', {'error': '비밀번호 확인이 일치하지 않습니다.'})
        if not PASSWORD_RE.match(password):
            return render(request, 'pages/join.html', {'error': '비밀번호는 10자 이상, 영문/숫자/특수문자를 포함해야 합니다.'})

        # 2) 이메일 인증 완료 확인
        v = request.session.get('email_verify')
        if not v or not v.get('verified') or v.get('email') != email:
            return render(request, 'pages/join.html', {'error': '이메일 인증을 먼저 완료해주세요.'})

        # 3) 사용자 생성 + 자동 로그인
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        request.session.pop('email_verify', None)
        return redirect('index')

    return render(request, 'pages/join.html')


def login_view(request):
    """아이디 또는 이메일로 로그인 지원(이메일은 case-insensitive)."""
    if request.method == 'POST':
        username_or_email = (request.POST.get('username') or '').strip()
        password = request.POST.get('password') or ''

        if '@' in username_or_email:
            # 이메일로 로그인 시도 (대소문자 무시)
            try:
                u = User.objects.get(email__iexact=username_or_email.strip().lower())
                username = u.username
            except User.DoesNotExist:
                username = username_or_email
        else:
            username = username_or_email

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'pages/login.html', {'error': '아이디/이메일 또는 비밀번호가 잘못되었습니다.'})

    return render(request, 'pages/login.html')

def logout_view(request):
    """로그아웃 처리"""
    logout(request)
    return redirect('index')

def dodam_view(request):
    """도담이 챗봇 페이지 - 로그인 필수"""
    if not request.user.is_authenticated:
        # 로그인 안 했으면 로그인 페이지로 리다이렉트 + 에러 메시지
        return render(request, 'pages/login.html', {
            'error': '로그인이 필요합니다!',
            'show_modal': True
        })
    return render(request, 'pages/model.html')


def chat_api(request):
    """
    런팟 API와 통신하여 챗봇 응답 생성
    프론트엔드에서 AJAX로 호출하는 API 엔드포인트
    """
    # POST 요청만 허용 (GET 요청은 거부)
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'POST만 허용'}, status=405)
    
    # 로그인 여부 확인 (로그인 안 하면 거부)
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': '로그인이 필요합니다'}, status=401)
    
    import json
    try:
        # 요청 본문(body)에서 JSON 데이터 파싱
        data = json.loads(request.body)
        question = data.get('question', '').strip()  # 사용자 질문
        history = data.get('history', [])  # 이전 대화 기록
        
        # 질문이 비어있으면 에러 반환
        if not question:
            return JsonResponse({'ok': False, 'error': '질문을 입력해주세요'})
        
        # 런팟 서버의 API URL (실제 배포 시 환경변수로 관리 권장)
        RUNPOD_API_URL = os.getenv("RUNPOD_API_URL", "https://qlele6r3nm2l34-8000.proxy.runpod.net/generate")
        
        # 런팟 API 키 (환경변수에서 가져오거나 직접 설정)
        RUNPOD_API_KEY = os.getenv('RUNPOD_API_KEY', '')  # 환경변수 사용 시
        # RUNPOD_API_KEY = ""  # 빈 값 = 인증 없음 (개발용)
        
        # 요청 헤더 설정 (API 키가 있으면 추가)
        headers = {'Content-Type': 'application/json'}
        if RUNPOD_API_KEY:
            headers['X-API-Key'] = RUNPOD_API_KEY
        
        # 런팟 API에 POST 요청 전송
        response = requests.post(
            RUNPOD_API_URL,
            headers=headers,
            json={
                'question': question,  # 사용자 질문
                'history': history,  # 대화 기록 (컨텍스트 유지)
                'max_new_tokens': 512,  # 생성할 최대 토큰 수
                'temperature': 0.2,  # 생성 다양성 (낮을수록 일관적)
                'top_p': 0.95  # nucleus sampling 파라미터
            },
            timeout=60  # 60초 타임아웃 (모델 응답 대기 시간)
        )
        
        # HTTP 에러 발생 시 예외 발생시킴
        response.raise_for_status()
        
        # 런팟 API 응답을 JSON으로 파싱
        result = response.json()
        
        # 성공 응답 반환 (프론트엔드로)
        return JsonResponse({
            'ok': True,
            'answer': result.get('answer') or result.get('text'),  # 답변 텍스트
            'mode': result.get('mode', 'chat'),  # 모드 (chat/search)
            'latency_ms': result.get('latency_ms', 0)  # 응답 시간
        })
        
    except requests.exceptions.Timeout:
        # 타임아웃 에러 (60초 내 응답 없음)
        return JsonResponse({'ok': False, 'error': '응답 시간 초과. 다시 시도해주세요.'})
    except requests.exceptions.RequestException as e:
        # 네트워크 에러 (연결 실패, HTTP 에러 등)
        return JsonResponse({'ok': False, 'error': f'서버 연결 오류: {str(e)}'})
    except Exception as e:
        # 기타 모든 에러 (JSON 파싱 실패 등)
        return JsonResponse({'ok': False, 'error': f'오류 발생: {str(e)}'})


# =========================
# 비밀번호 찾기
# =========================
def password_reset_view(request):
    """비밀번호 찾기 페이지 + 비밀번호 재설정 처리"""
    if request.method == 'POST':
        email = (request.POST.get('email') or '').strip().lower()
        password = request.POST.get('password') or ''

        # 1) 이메일 인증 완료 확인
        v = request.session.get('password_reset_verify')
        if not v or not v.get('verified') or v.get('email') != email:
            return render(request, 'pages/password_reset.html', {'error': '이메일 인증을 먼저 완료해주세요.'})

        # 2) 비밀번호 유효성 검사
        if not PASSWORD_RE.match(password):
            return render(request, 'pages/password_reset.html', {'error': '비밀번호는 10자 이상, 영문/숫자/특수문자를 포함해야 합니다.'})

        # 3) 해당 이메일의 사용자 찾아서 비밀번호 변경
        try:
            user = User.objects.get(email__iexact=email)
            user.set_password(password)
            user.save()
            request.session.pop('password_reset_verify', None)
            return redirect('login')
        except User.DoesNotExist:
            return render(request, 'pages/password_reset.html', {'error': '해당 이메일로 가입된 계정이 없습니다.'})

    return render(request, 'pages/password_reset.html')


def password_reset_send_code(request):
    """비밀번호 찾기: 이메일 인증 코드 전송"""
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'reason': 'POST만 허용'}, status=405)

    email = (request.POST.get('email') or '').strip().lower()
    if not email or '@' not in email or '.' not in email:
        return JsonResponse({'ok': False, 'reason': '이메일 형식이 올바르지 않습니다.'})

    # 해당 이메일로 가입된 계정이 있는지 확인
    if not User.objects.filter(email__iexact=email).exists():
        return JsonResponse({'ok': False, 'reason': '가입되지 않은 이메일입니다.'})

    now_ts = int(timezone.now().timestamp())
    data = request.session.get('password_reset_verify')

    # 동일 이메일 + 유효시간 내 재요청 → 남은 초 안내 후 차단
    if data and data.get('email') == email and isinstance(data.get('expires_ts'), int):
        remain = data['expires_ts'] - now_ts
        if remain > 0:
            return JsonResponse({
                'ok': False,
                'blocked': 'cooldown',
                'remain': remain,
                'reason': f'이미 전송됨. {remain}초 뒤 다시 시도하세요.'
            })

    # 새 코드 발급
    code = f"{random.randint(100000, 999999)}"
    expires_ts = int((timezone.now() + timedelta(minutes=5)).timestamp())
    request.session['password_reset_verify'] = {
        'email': email,
        'code': code,
        'expires_ts': expires_ts,
        'verified': False,
    }

    send_mail(
        subject='[베이비가이드] 비밀번호 재설정 인증 코드',
        message=f'인증 코드: {code} (5분 내 유효)',
        from_email=None,
        recipient_list=[email],
        fail_silently=True,
    )
    return JsonResponse({'ok': True, 'message': '인증번호가 발송되었습니다.', 'expires_in': 300})


def password_reset_verify_code(request):
    """비밀번호 찾기: 이메일 인증 코드 검증"""
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'reason': 'POST만 허용'}, status=405)

    email = (request.POST.get('email') or '').strip().lower()
    code = (request.POST.get('code') or '').strip()

    data = request.session.get('password_reset_verify')
    if not data:
        return JsonResponse({'ok': False, 'reason': '인증 요청을 먼저 해주세요.'})
    if data.get('email') != email:
        return JsonResponse({'ok': False, 'reason': '요청한 이메일과 다릅니다.'})

    now_ts = int(timezone.now().timestamp())
    expires_ts = data.get('expires_ts')
    if not isinstance(expires_ts, int):
        return JsonResponse({'ok': False, 'reason': '세션 정보가 올바르지 않습니다. 다시 요청하세요.'})
    if now_ts > expires_ts:
        return JsonResponse({'ok': False, 'reason': '인증 유효시간(5분) 만료. 재요청하세요.'})

    if data.get('code') != code:
        return JsonResponse({'ok': False, 'reason': '인증번호가 일치하지 않습니다.'})

    data['verified'] = True
    request.session['password_reset_verify'] = data
    return JsonResponse({'ok': True, 'message': '이메일 인증이 완료되었습니다.'})