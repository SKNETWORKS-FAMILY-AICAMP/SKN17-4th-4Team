# 👶 육아 도우미(ParentCare) 프로젝트

**도담이(챗봇)**를 중심으로 육아 정보를 신속·친절하게 안내하는 경량 웹 서비스입니다. 본 버전은 **챗봇 + 인증(로그인/회원가입) + 홈 랜딩**으로 구성됩니다.

---

## 목차

1. [팀 소개](#-팀-소개)
2. [프로젝트 개요](#-프로젝트-개요)
3. [WBS](#-WBS)
4. [기술 스택 & 사용 모델](#-기술-스택-&-사용-모델)
5. [시스템 구성도](#-시스템-구성도)
6. [핵심 기능](#-핵심-기능)
7. [요구사항 정의](#-요구사항-정의)
8. [화면 설계서](#-화면-설계서)
9. [테스트 계획 및 결과](#-테스트-계획-및-결과)
10. [실행 방법](#-실행-방법)
11. [향후 과제](#-향후-과제)
12. [한줄 회고록](#-한줄-회고록)

## 1. 팀 소개

| 이름  | GitHub ID  |
| --- | ---------- |
| 김민균 | <a href="https://github.com/alswhitetiger">@alswhitetiger</a></td> |
| 김세한 | <a href="https://github.com/kimsehan11">@kimsehan11</a></td> |
| 김수현 | <a href="https://github.com/K-SH98">@K-SH98</a></td> |
| 정의중 | <a href="https://github.com/uii42">@uii42</a></td> |
| 최우진 | <a href="https://github.com/CHUH00">@CHUH00</a></td> |

---

## 2. 프로젝트 개요

### 2-1) 문제정의

* 육아 정보가 분산되어 있어 **즉시 접근**이 어렵고, 긴급 상황에서 **요약된 가이드**가 필요함.

### 2-2) 목표

* 챗봇 **도담이**를 통해 질문-답변을 **빠르게 제공**
* 신뢰 가능한 출처 기반 응답(출처/갱신일 표시)
* 로그인/회원가입으로 **개인화 기본 토대** 제공 (향후 알림/히스토리 확장 대비)

### 2-3) 범위(Scope)

* 포함: 홈 랜딩, 로그인, 회원가입, **챗봇(대화/저장)**

---

## 3. 작업 계획

> **기간: 2일(데모/발표용 스프린트)**

| Day    | 마일스톤           | 상세 작업                                         | 산출물                  |
| ------ | -------------- | --------------------------------------------- | -------------------- |
| 1일차 오전 | 리포 세팅          | README/이슈·PR 템플릿/브랜치 규칙 적용, CI 스켈레톤           | 초기 커밋, CI 통과         |
| 1일차 오후 | 화면 마크업 1       | **메인 홈(scr-main-01)**, **로그인(scr-signin-01)** | 화면 초안, 라우팅           |
| 2일차 오전 | 화면 마크업 2       | **회원가입(scr-signup-01)**, **챗봇(scr-chat-01)**  | 화면 초안, 상태/폼 검증       |
| 2일차 오후 | API 목/연동 & 테스트 | 가짜 API/JSON 서버, 가입/로그인 흐름, 간단 E2E             | 데모 빌드(v0.1), 테스트 결과표 |

* 위험/대응: 데이터 지연 ▶ 목API로 대체, 이미지 미확정 ▶ 플레이스홀더 사용\

---
## 4. 기술 스택 & 사용 모델

**개발 도구**
[![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode\&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker\&logoColor=white)](#)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-2496ED?logo=docker\&logoColor=white)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git\&logoColor=white)](#)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions\&logoColor=white)](#)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?logo=postman\&logoColor=white)](#)

**개발 언어**
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript\&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white)](#)

**벡터 DB**
[![FAISS](https://img.shields.io/badge/FAISS-0055FF?logo=vectorworks\&logoColor=white)](#)

**사용하는 모델**
[![GPT-4o mini](https://img.shields.io/badge/GPT--4o%20mini-412991?logo=openai\&logoColor=white)](#)
[![text-embedding-3-large](https://img.shields.io/badge/text--embedding--3--large-412991?logo=openai\&logoColor=white)](#)

**서버**
[![Django](https://img.shields.io/badge/Django-092E20?logo=django\&logoColor=white)](#)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-1F9AFE?logo=fastapi\&logoColor=white)](#)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn\&logoColor=white)](#)
[![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx\&logoColor=white)](#)

**서비스 제공자**
[![AWS](https://img.shields.io/badge/AWS-FF9900?logo=amazonwebservices\&logoColor=white)](#)

**데이터베이스**
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql\&logoColor=white)](#)

**협력 도구**
[![Slack](https://img.shields.io/badge/Slack-4A154B?logo=slack\&logoColor=white)](#)
[![Notion](https://img.shields.io/badge/Notion-000000?logo=notion\&logoColor=white)](#)
[![Figma](https://img.shields.io/badge/Figma-F24E1E?logo=figma\&logoColor=white)](#)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?logo=googledrive\&logoColor=white)](#)


---

## 5. 시스템 구성도

```
[Client: Web/Mobile]
        |
        v
[API Gateway / Nginx]
        |
        v
[Backend: Django/DRF] --- [Auth(JWT/OAuth)]
        |                       |
        v                       v
   [PostgreSQL]            [Object Storage(S3)]
        |
        v
[ETL/Data Jobs] <--- [공공데이터/의료기관/보건소 API]
```

아키텍처 다이어그램(이미지):\

---

## 6. 핵심 기능

* **도담이 챗봇**: 자연어 질의에 대한 요약형 답변, 출처/갱신일 표기, 최근 대화 **.txt 저장**
* **인증**: 이메일 로그인/회원가입(닉네임/이메일/비밀번호 규칙/인증번호)
* **홈 랜딩**: 서비스 소개, 챗봇 시작 CTA, 푸터(운영사/저작권)

---

## 7. 요구사항 정의

<img width="1288" height="707" alt="image" src="https://github.com/user-attachments/assets/e0cf3b02-0898-4c72-966a-6c1c89e4decd" />


---

## 8. API 설계

> 핵심 엔드포인트만 명시 (예시)

| 메서드  | 경로                            | 설명                       |
| ---- | ----------------------------- | ------------------------ |
| POST | `/api/auth/signup`            | 회원가입(닉네임/이메일/비밀번호)       |
| POST | `/api/auth/login`             | 로그인(JWT 발급)              |
| POST | `/api/chat/ask`               | 질문 전송 → 답변 반환(출처/갱신일 포함) |
| GET  | `/api/chat/export?format=txt` | 최근 대화 내보내기               |

응답 예시(챗봇):

```json
{
  "answer": "모유 수유 중 음식 권장사항은...",
  "sources": [
    {"title": "보건복지부 가이드", "url": "https://...", "updated_at": "2025-10-20"}
  ]
}
```

---- | ----------------------------- | ------------------------ |
| POST | `/api/auth/signup`            | 회원가입(닉네임/이메일/비밀번호)       |
| POST | `/api/auth/login`             | 로그인(JWT 발급)              |
| POST | `/api/chat/ask`               | 질문 전송 → 답변 반환(출처/갱신일 포함) |
| GET  | `/api/chat/export?format=txt` | 최근 대화 내보내기               |

응답 예시(챗봇):

```json
{
  "answer": "모유 수유 중 음식 권장사항은...",
  "sources": [
    {"title": "보건복지부 가이드", "url": "https://...", "updated_at": "2025-10-20"}
  ]
}
```


응답 예시:

```json
{
  "items": [
    {
      "id": 123,
      "name": "행복소아과의원",
      "lat": 37.51,
      "lng": 127.02,
      "night_service": true,
      "phone": "02-123-4567"
    }
  ],
  "total": 1
}
```

---

## 9. 화면 설계서

### 9-1) 메인 홈 화면 (`scr-home-01`)

<img width="1382" height="758" alt="image" src="https://github.com/user-attachments/assets/f665a7f2-87a0-4c45-9c28-f922d4b0aeb6" />


---

### 9-2) 로그인 화면 (`scr-user-01`)

<img width="1384" height="754" alt="image" src="https://github.com/user-attachments/assets/d3be6c2d-dae0-4b96-b6ab-c340f9bbf2c8" />


---

### 9-3) 회원가입 화면 (`scr-user-02`)

<img width="1384" height="761" alt="image" src="https://github.com/user-attachments/assets/9c669893-c8e6-484c-a61c-72107103e0eb" />


---

### 9-4) 챗봇 화면 (`scr-chat-01`)

<img width="1387" height="756" alt="image" src="https://github.com/user-attachments/assets/669db2d4-649d-4b38-9b17-9a6b9b413adb" />

---

## 10. 테스트 계획 및 결과

### 10-1) 테스트 계획

| ID           | 시나리오        | 절차                    | 기대 결과                          |
| ------------ | ----------- | --------------------- | ------------------------------ |
| TC-LOGIN-01  | 이메일 로그인 성공  | 올바른 계정 입력 → 로그인       | 홈 이동, 세션 생성                    |
| TC-LOGIN-02  | 이메일 로그인 실패  | 잘못된 비밀번호 입력           | 오류 토스트(3-1) 노출                 |
| TC-SIGNUP-01 | 인증 메일 발송/검증 | 이메일 입력 → 인증요청 → 코드 입력 | 1분 내 메일 수신·검증 통과               |
| TC-CHAT-01   | 기본 질의/응답    | 질문 입력 → 응답 확인         | 3s p95 이내 답변 표시                |
| TC-CHAT-02   | 대화 저장       | 저장 버튼 클릭              | `dodam_YYYYMMDD_HHMM.txt` 다운로드 |

### 10-2) 결과(예시)

| ID          | 결과   | 비고       |
| ----------- | ---- | -------- |
| TC-LOGIN-01 | Pass | 200ms 응답 |
| TC-CHAT-01  | Pass | 2.5s p95 |

---|---|---|---|
| TC-001 | 위치 기반 병원 조회 | 위치 허용 → 야간 필터 On | 야간 진료 병원만 표시 |
| TC-010 | 접종 알림 | DOB 입력 → 접종 달 도래 | 알림 수신(앱/메일) |
| TC-020 | 신고/블라인드 | 동일 게시물 3회 신고 | 자동 블라인드 처리 |

### 10-2) 결과(예시)

| ID     | 결과   | 비고            |
| ------ | ---- | ------------- |
| TC-001 | Pass | 응답 450ms p95  |
| TC-010 | Pass | 메일 도착 30초 내   |
| TC-020 | Pass | 운영자 페이지 로그 확인 |


---

## 11. 실행 방법

### 11-1) 환경 변수

`.env` (예시)

```
DATABASE_URL=postgresql://user:pass@host:5432/parentcare
JWT_SECRET=replace_me
MAPS_API_KEY=replace_me
```

### 11-2) 로컬(예: Node + Django 혼합 리포일 때)

```bash
# Frontend
cd frontend
npm i
npm run dev

# Backend
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 11-3) 도커(옵션)

```bash
docker compose up -d --build
```

---

## 12. 폴더 구조

```
.
├─ frontend/               # React, Vite
│  ├─ src/
│  └─ ...
├─ backend/                # Django/DRF
│  ├─ app/
│  └─ ...
├─ docs/
│  ├─ architecture.png
│  └─ ui/
│     ├─ home.png
│     ├─ signin.png
│     ├─ signup.png
│     └─ chat.png
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ bug_report.yml
│  │  └─ feature_request.yml
│  └─ pull_request_template.md
├─ .env.example
└─ README.md
```

---

## 14. 향후 과제

* 푸시 알림(모바일/PWA) 정교화, 다자녀 프로필 지원
* 의료기관/약국 실시간 혼잡도·대기시간 연동
* 신뢰성 검증(출처) 자동 업데이트 및 변경 알림
* 챗봇 증강(RAG) 정답률 지표화, 금칙어/응급 가이드 보강
* 접근성 개선(색대비/키보드 내비/스크린리더)

---

## 한줄 회고록
* 김민균:
* 김세한:
* 김수현:
* 정의중:
* 최우진:
