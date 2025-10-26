# 🚀 베이비가이드 배포 가이드

## 목차
1. [런팟(RunPod) 서버 설정](#1-런팟runpod-서버-설정)
2. [Django 연동 설정](#2-django-연동-설정)
3. [AWS EC2 배포](#3-aws-ec2-배포)
4. [서버 관리](#4-서버-관리)

---

## 1. 런팟(RunPod) 서버 설정

### 1.1 초기 설정

#### Pod 생성 및 환경변수 설정
1. RunPod 웹사이트에서 GPU Pod 생성
2. **Environment Variables** 설정:
   ```
   MODEL_ID=WOOJINIYA/parentcare-bot-qwen2.5-7b
   HF_EMBED_REPO_ID=WOOJINIYA/parentcare-bot-bge-m3
   FAISS_INDEX_PATH=/workspace/index/faiss.index
   FAISS_META_PATH=/workspace/index/faiss.meta.json
   API_KEY=너 키 넣으면 됨                     # 빈 값으로 설정 (개발 모드)
   KAKAO_API_REST_KEY=your_key  # 선택사항
   HIRA_API_SERVICE_KEY=your_key # 선택사항
   ```

3. **Expose HTTP Ports** 설정:
   - HTTP Port: `8000` 추가
   - SSH Port: `22` (기본값)

4. Pod 저장 및 시작

---

### 1.2 파일 구조 설정

#### Jupyter Lab으로 접속 (Port 8888)
1. RunPod 대시보드에서 **Jupyter Lab** 버튼 클릭
2. 터미널 열기

#### 디렉토리 생성
```bash
cd /workspace
mkdir -p app index
```

#### 파일 업로드
- `/workspace/app/` 폴더에:
  - `app.py` (FastAPI 서버 코드)
  
- `/workspace/index/` 폴더에:
  - `faiss.index` (벡터 인덱스 파일)
  - `faiss.meta.json` (메타데이터 파일)

- `/workspace/requirements.txt` -> install

---

### 1.3 필요한 라이브러리 설치

```bash
# SSH 접속 (VS Code Git Bash 또는 터미널)
ssh <pod-id>@ssh.runpod.io -i ~/.ssh/id_ed25519

# 라이브러리 설치
pip install torch transformers sentence-transformers faiss-gpu-cu12 fastapi uvicorn pydantic requests numpy hf-transfer -> 걍 pip install -r requirements.txt 하면 됨
```

**CUDA 버전 확인:** -> 요거는 requirements.txt 할 때 runpod에 nvidia-smi 쳐서 version 확인하고 저거에 맞게 해야함
```bash
nvidia-smi  # CUDA Version 확인
# CUDA 12.x → faiss-gpu-cu12
# CUDA 11.x → faiss-gpu-cu11
```

---

### 1.4 서버 실행

```bash
cd /workspace/app
uvicorn app:app --host 0.0.0.0 --port 8000

그리고 동시에 같은 포트로 실행 안되니까 다시 실행하려면 kill -9 pid 해야함 
```

**정상 실행 시 출력:**
```
[boot] LLM 로딩 완료.
[boot] 임베딩 모델 로딩 완료.
[boot] FAISS 인덱스 로딩 완료.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

### 1.5 API 테스트

#### Health Check
```bash
curl https://<pod-id>-8000.proxy.runpod.net/health
# 응답: {"ok":true}
```

#### 실제 질문 테스트
```bash
curl -X POST https://<pod-id>-8000.proxy.runpod.net/generate \
  -H "Content-Type: application/json" \
  -d '{"question":"아기가 열이 나는데 어떻게 해야 하나요?"}'
```

---

## 2. Django 연동 설정

### 2.1 코드 수정

#### `views.py`에 런팟 API 호출 함수 추가
```python
import requests
import os

def chat_api(request):
    """런팟 API와 통신하여 챗봇 응답 생성"""
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'POST만 허용'}, status=405)
    
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': '로그인이 필요합니다'}, status=401)
    
    import json
    try:
        data = json.loads(request.body)
        question = data.get('question', '').strip()
        history = data.get('history', [])
        
        if not question:
            return JsonResponse({'ok': False, 'error': '질문을 입력해주세요'})
        
        # 런팟 API URL
        RUNPOD_API_URL = "https://<your-pod-id>-8000.proxy.runpod.net/generate"
        
        # API 키 설정 (빈 값 = 인증 없음)
        RUNPOD_API_KEY = ""
        
        # 헤더 설정
        headers = {'Content-Type': 'application/json'}
        if RUNPOD_API_KEY:
            headers['X-API-Key'] = RUNPOD_API_KEY
        
        # 런팟 API 호출
        response = requests.post(
            RUNPOD_API_URL,
            headers=headers,
            json={
                'question': question,
                'history': history,
                'max_new_tokens': 512,
                'temperature': 0.2,
                'top_p': 0.95
            },
            timeout=60
        )
        
        response.raise_for_status()
        result = response.json()
        
        return JsonResponse({
            'ok': True,
            'answer': result.get('answer') or result.get('text'),
            'mode': result.get('mode', 'chat'),
            'latency_ms': result.get('latency_ms', 0)
        })
        
    except requests.exceptions.Timeout:
        return JsonResponse({'ok': False, 'error': '응답 시간 초과. 다시 시도해주세요.'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'ok': False, 'error': f'서버 연결 오류: {str(e)}'})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': f'오류 발생: {str(e)}'})
```

#### `urls.py`에 경로 추가
```python
from django.urls import path
from . import views

urlpatterns = [
    # ... 기존 경로들 ...
    path('api/chat/', views.chat_api, name='api_chat'),
]
```

#### `model.html` JavaScript로 동적 챗봇 구현
```javascript
// AJAX로 Django API 호출
fetch('/api/chat/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': getCSRFToken()
  },
  body: JSON.stringify({
    question: question,
    history: chatHistory
  })
})
.then(response => response.json())
.then(data => {
  if (data.ok) {
    // 봇 응답 표시
    addMessage(data.answer, false);
  }
});
```

---

### 2.2 requirements.txt 업데이트

`requests` 라이브러리 추가:
```txt
Django==4.2.7
django-cors-headers==4.3.0
django-filter==23.3
djangorestframework==3.14.0
mysqlclient==2.2.0
python-decouple==3.8
uvicorn[standard]==0.24.0
whitenoise==6.6.0
requests==2.31.0  # 추가
```

---

## 3. AWS EC2 배포

### 3.1 사전 준비

- AWS EC2 인스턴스 생성 완료
- SSH 키 파일 (`team_4.pem`) 준비
- 보안 그룹에서 포트 8000 오픈

---

### 3.2 배포 프로세스

#### 1. 로컬에서 코드 업데이트
```bash
cd C:/Users/Playdata/OneDrive/Desktop/TEAM_4/parent_bot_project

# 변경사항 커밋
git add .
git commit -m "connect with ai"
git push origin main
```

#### 2. EC2 서버 접속
```bash
# Git Bash 또는 터미널에서
ssh -i team_4.pem ubuntu@13.124.52.49

이 상태에서 도커 안올라와 있으면 docker-compose up -d 하면 되고 뭔가 수정사항 생기면 걍 
docker-compose down -> docker-compose docker-compose build --no-cache -> docker-compose up -d 하면 됨
참고로 -d 는 백그라운드 실행임 로그 남기고 싶으면 -d 없애면 됨.
```

#### 3. 코드 업데이트
```bash
cd ~/SKN17-4th-4Team
git pull origin main
```

#### 4. Docker 재빌드 및 실행
```bash
# 기존 컨테이너 중지
docker-compose down

# 캐시 없이 재빌드 (requirements.txt 변경 시 필수)
docker-compose build --no-cache

# 백그라운드로 실행
docker-compose up -d

# 로그 확인
docker-compose logs -f
```

#### 5. 서버 상태 확인
```bash
# 컨테이너 상태
docker-compose ps

# Django 로그
docker-compose logs web -f

# MySQL 로그
docker-compose logs mysql -f
```

---

### 3.3 문제 해결

#### requests 모듈 에러 발생 시
```bash
# Docker 재빌드 필수
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

#### 데이터베이스 연결 실패 시
```bash
# MySQL 컨테이너 확인
docker-compose ps mysql

# MySQL 재시작
docker-compose restart mysql
```

---

## 4. 서버 관리

### 4.1 런팟(RunPod) 관리

#### 서버 시작
```bash
# SSH 접속
ssh <pod-id>@ssh.runpod.io -i ~/.ssh/id_ed25519

# 서버 실행
cd /workspace/app
uvicorn app:app --host 0.0.0.0 --port 8000
```

#### 백그라운드 실행 (SSH 연결 끊어져도 계속 실행)
```bash
nohup uvicorn app:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &

# 로그 확인
tail -f server.log
```

#### 프로세스 관리
```bash
# 실행 중인 uvicorn 찾기
ps aux | grep uvicorn

# 특정 프로세스 종료
kill -9 <PID>

# 모든 uvicorn 종료
killall -9 python3
```

#### 비용 절감
- **사용 안 할 때**: RunPod 대시보드에서 **Stop** 버튼 클릭
- **데이터 보존**: `/workspace/` 폴더는 Pod 재시작 후에도 유지됨
- **비용**: Running 상태일 때만 GPU 비용 발생 (약 $0.3~$0.5/시간)

---

### 4.2 AWS EC2 관리

#### Docker 컨테이너 관리
```bash
# 시작
docker-compose up -d

# 중지
docker-compose down

# 재시작
docker-compose restart

# 로그 실시간 확인
docker-compose logs -f

# 특정 서비스만 재시작
docker-compose restart web
```

#### EC2 인스턴스 관리
- **중지**: AWS 콘솔 → Instances → Stop (컴퓨팅 비용 절약)
- **시작**: AWS 콘솔 → Instances → Start
- **주의**: Stop 시에도 스토리지 비용 발생 (매우 저렴)

---

### 4.3 전체 시스템 시작 순서

#### 1. 런팟 서버 시작
```bash
# RunPod 대시보드에서 Pod Start
# SSH 접속 후
cd /workspace/app
uvicorn app:app --host 0.0.0.0 --port 8000
```

#### 2. EC2 서버 시작
```bash
# AWS 콘솔에서 EC2 Start (또는 이미 실행 중)
# SSH 접속 후
cd ~/SKN17-4th-4Team
docker-compose up -d
```

#### 3. 접속 확인
- **Django**: `http://13.124.52.49:8000/`
- **런팟 Health Check**: `https://<pod-id>-8000.proxy.runpod.net/health`

---

### 4.4 로그 확인 방법

#### 런팟 로그
```bash
# SSH 접속 중인 터미널에서 실시간 확인
# 또는 nohup 사용 시
tail -f /workspace/app/server.log
```

#### Django 로그 (EC2)
```bash
# Docker 컨테이너 로그
docker-compose logs web -f

# 또는 시스템 로그
sudo journalctl -u docker -f
```

---

## 5. 주의사항

### 5.1 보안

- **.env 파일**: Git에 절대 올리지 말 것 (`.gitignore`에 추가)
- **SECRET_KEY**: 강력한 키로 변경
- **API_KEY**: 배포 시에는 강력한 키 설정 권장
- **SSH 키**: `team_4.pem` 파일 보안 유지

### 5.2 비용

- **런팟**: 사용 안 할 때 반드시 Stop
- **EC2**: 장기간 미사용 시 Stop
- **데이터**: Stop 해도 `/workspace/` 및 EBS 볼륨 데이터는 유지됨

### 5.3 백업

- **코드**: 정기적으로 Git push
- **데이터베이스**: 주기적으로 백업
- **FAISS 인덱스**: 런팟 `/workspace/` 외부에도 백업

---

## 6. 트러블슈팅

### 401 Unauthorized 에러
- 런팟 `API_KEY` 환경변수 확인 (빈 값으로 설정)
- Pod 재시작 후 환경변수 적용 확인

### 500 Internal Server Error
- Django 로그 확인: `docker-compose logs web -f`
- `requests` 모듈 설치 확인
- Docker 재빌드 필요 시: `docker-compose build --no-cache`

### Connection Timeout
- 런팟 서버 실행 확인: `ps aux | grep uvicorn`
- HTTP 포트(8000) 노출 확인
- Health check URL 테스트

### FAISS 파일 에러
- 파일 크기 확인: `ls -lh /workspace/index/`
- 파일 재업로드 필요 시 Jupyter Lab 사용

---

## 7. 참고 링크

- **RunPod 문서**: https://docs.runpod.io/
- **Django 문서**: https://docs.djangoproject.com/
- **FastAPI 문서**: https://fastapi.tiangolo.com/
- **Docker Compose 문서**: https://docs.docker.com/compose/

---

## 연락처

문제 발생 시 팀원에게 문의하거나 이슈를 등록해주세요.

**프로젝트**: SKN17-4th-4Team  
**GitHub**: https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-4th-4Team
