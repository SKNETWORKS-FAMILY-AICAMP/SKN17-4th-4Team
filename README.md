# 👶 베이비가이드 프로젝트

## 프로젝트 개요

- **목표**: 부모님을 위한 AI 챗봇 및 정보 제공 서비스
- **주요 기능**:
  - AI 챗봇 (런팟 GPU 서버 + RAG)
  - 병원/약국 검색
  - 회원가입/로그인/비밀번호 찾기
  - 반응형 웹 UI

---

## 기술 스택

- **백엔드**: Django 4.2, djangorestframework
- **AI 서버**: FastAPI (런팟, Hugging Face Transformers, FAISS)
- **DB**: MySQL (Docker)
- **프론트엔드**: HTML, CSS, JavaScript (Django Template)
- **배포**: AWS EC2 (Docker Compose), RunPod (GPU)

---

## 시스템 아키텍처

```
[사용자 브라우저]
      │
      ▼
[AWS EC2: Django + MySQL]
      │   └─(API 호출)─▶ [RunPod: FastAPI + LLM + FAISS]
      │
      ▼
[DB, 정적 파일, 템플릿]
```

- **Django**: 사용자 인증, 챗봇 UI, API 중계
- **RunPod**: LLM(7B), 임베딩, RAG, 병원/약국 검색

---

## 배포/운영 요약

### 1. RunPod (AI 서버)
- Pod 생성, 환경변수/포트 설정
- `/workspace/app/app.py`, `/workspace/index/faiss.index` 등 업로드
- `pip install -r requirements.txt`
- `uvicorn app:app --host 0.0.0.0 --port 8000`
- Health Check: `https://<pod-id>-8000.proxy.runpod.net/health`

### 2. AWS EC2 (Django)
- `git pull origin main`
- `docker-compose up -d` (최초/수정 시 재시작)
- 접속: `http://<EC2-IP>:8000/`

---

## 주요 폴더 구조

```
parent_bot_project_main/
  ├─ babyguide/         # Django 설정
  ├─ core/             # Django 앱 (views, urls 등)
  ├─ static/           # CSS, 이미지
  ├─ templates/        # HTML 템플릿
  └─ manage.py
runpod_server/
  └─ app.py            # FastAPI 서버 (런팟)
  └─ index/            # FAISS 인덱스 파일
```

---

## 개발/운영 팁

- **런팟**: `/workspace/` 폴더만 영구 저장, 나머지는 Stop 시 삭제
- **EC2**: `team_4.pem` 키로 SSH 접속, 도커 재시작 필요 시 `docker-compose down && docker-compose up -d`
- **API 연동**: `core/views.py`에서 RunPod API URL/KEY 관리
- **정적 파일**: CSS/JS만 바꿀 땐 도커 재시작 불필요, Python 코드 바꿀 땐 재시작 필수
- **비용**: 런팟/EC2 둘 다 사용 안 할 때 반드시 Stop

---

## 트러블슈팅

- **런팟 401/404**: Pod ID, API_KEY, 서버 실행 상태 확인
- **EC2 접속 불가**: 퍼블릭 IP, 보안그룹(22번), 키파일 권한 확인
- **DB 에러**: `docker-compose logs mysql -f`로 로그 확인
- **모델 느림**: 첫 실행시 모델/임베딩 다운로드, 이후 캐시 사용

---

## 참고
- [런팟 공식문서](https://docs.runpod.io/)
- [Django 공식문서](https://docs.djangoproject.com/)
- [FastAPI 공식문서](https://fastapi.tiangolo.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

**문의/이슈**: 팀원 또는 GitHub 이슈로 연락

