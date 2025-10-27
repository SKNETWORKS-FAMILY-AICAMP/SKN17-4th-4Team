# 👶 육아 도우미(ParentCare) 프로젝트

**도담이(챗봇)**를 중심으로 육아 정보를 신속·친절하게 안내하는 경량 웹 서비스입니다. 본 버전은 **챗봇 + 인증(로그인/회원가입) + 홈 랜딩**으로 구성됩니다.

---

## 목차

- [1. 팀 소개](#1-팀-소개)
- [2. 프로젝트 개요](#2-프로젝트-개요)
  - [2-1) 문제정의](#2-1-문제정의)
  - [2-2) 목표](#2-2-목표)
  - [2-3) 범위(Scope)](#2-3-범위scope)
- [3. WBS](#3-wbs)
- [4. 기술 스택 & 사용 모델](#4-기술-스택--사용-모델)
- [5. 시스템 구성도](#5-시스템-구성도)
- [6. 핵심 기능](#6-핵심-기능)
- [7. 요구사항 정의](#7-요구사항-정의)
- [8. 화면 설계서](#8-화면-설계서)
  - [8-1) 메인 홈 화면 (`scr-home-01`)](#8-1-메인-홈-화면-scr-home-01)
  - [8-2) 로그인 화면 (`scr-user-01`)](#8-2-로그인-화면-scr-user-01)
  - [8-3) 회원가입 화면 (`scr-user-02`)](#8-3-회원가입-화면-scr-user-02)
  - [8-4) 챗봇 화면 (`scr-chat-01`)](#8-4-챗봇-화면-scr-chat-01)
- [9. 테스트 계획 및 결과](#9-테스트-계획-및-결과)
  - [9-1) 테스트 계획](#9-1-테스트-계획)
  - [9-2) 결과(예시)](#9-2-결과예시)
- [10. 향후 과제](#10-향후-과제)
- [11. 한줄 회고록](#11-한줄-회고록)

---

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
* 로그인/회원가입으로 **개인화 기본 토대** 제공

### 2-3) 범위(Scope)

* 포함: 홈 랜딩, 로그인, 회원가입, **챗봇(대화/저장)**

---

## 3. WBS



---
## 4. 기술 스택 & 사용 모델

**개발 도구**  
[![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](#)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-2496ED?style=flat&logo=docker&logoColor=white)](#)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)](#)

**개발 언어**  
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](#)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](#)

**벡터 DB**  
[![FAISS](https://img.shields.io/badge/FAISS-00A39B?style=flat&logo=meta&logoColor=white)](#)

**사용하는 모델**  
[![Embedding: bge-m3](https://img.shields.io/badge/Embedding-bge--m3-4C9EE3?style=flat&logo=huggingface&logoColor=white)](https://huggingface.co/WOOJINIYA/parentcare-bot-bge-m3)
[![LLM: Qwen2.5-7B](https://img.shields.io/badge/LLM-Qwen2.5--7B-6E56CF?style=flat&logo=huggingface&logoColor=white)](https://huggingface.co/WOOJINIYA/parentcare-bot-qwen2.5-7b)

**서버**  
[![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat&logo=amazonwebservices&logoColor=white)](#)
[![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)](#)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat&logo=gunicorn&logoColor=white)](#)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white)](#)

**서비스 제공자**  
[![RunPod](https://img.shields.io/badge/RunPod-2E7D32?style=flat&logo=cloud&logoColor=white)](https://www.runpod.io/console)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](#)

**데이터베이스**  
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)](https://dev.mysql.com/doc/)

**협력 도구**  
[![Notion](https://img.shields.io/badge/Notion-000000?style=flat&logo=notion&logoColor=white)](#)
[![Figma](https://img.shields.io/badge/Figma-F24E1E?style=flat&logo=figma&logoColor=white)](#)
[![GitHub](https://img.shields.io/badge/GitHub-000000?style=flat&logo=github&logoColor=white)](https://github.com/)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=white)](#)



---

## 5. 시스템 구성도

<img width="532" height="305" alt="image" src="https://github.com/user-attachments/assets/f490b0bf-aed4-441c-832b-3b50a4d1801a" />


---

## 6. 핵심 기능

* **도담이 챗봇**: 자연어 질의에 대한 요약형 답변, 출처/갱신일 표기, 최근 대화 **.txt 저장**
* **인증**: 이메일 로그인/회원가입(닉네임/이메일/비밀번호 규칙/인증번호)
* **홈 랜딩**: 서비스 소개, 챗봇 시작 CTA, 푸터(운영사/저작권)

---

## 7. 요구사항 정의

<img width="1286" height="779" alt="image" src="https://github.com/user-attachments/assets/4e8e4de5-cb7a-4334-9735-a536860b3027" />


---

## 8. 화면 설계서

### 8-1) 메인 홈 화면 (`scr-home-01`)

<img width="1381" height="784" alt="image" src="https://github.com/user-attachments/assets/abd08362-4550-4739-bed1-eee98e32221f" />



---

### 8-2) 로그인 화면 (`scr-user-01`)

<img width="1380" height="786" alt="image" src="https://github.com/user-attachments/assets/4e2637d9-2b27-4549-8269-167210a0367b" />



---

### 8-3) 회원가입 화면 (`scr-user-02`)

<img width="1376" height="774" alt="image" src="https://github.com/user-attachments/assets/136588aa-4660-475e-8117-dd8effe3db84" />



---

### 8-4) 챗봇 화면 (`scr-chat-01`)

<img width="1385" height="793" alt="image" src="https://github.com/user-attachments/assets/62219abf-0fe9-4b08-a79b-69ea27ae33ec" />


---

## 9. 테스트 계획 및 결과

### 9-1) 테스트 계획

| ID           | 시나리오        | 절차                    | 기대 결과                          |
| ------------ | ----------- | --------------------- | ------------------------------ |
| TC-LOGIN-01  | 이메일 로그인 성공  | 올바른 계정 입력 → 로그인       | 홈 이동, 세션 생성                    |
| TC-LOGIN-02  | 이메일 로그인 실패  | 잘못된 비밀번호 입력           | 오류 토스트(3-1) 노출                 |
| TC-SIGNUP-01 | 인증 메일 발송/검증 | 이메일 입력 → 인증요청 → 코드 입력 | 1분 내 메일 수신·검증 통과               |
| TC-CHAT-01   | 기본 질의/응답    | 질문 입력 → 응답 확인         | 3s p95 이내 답변 표시                |
| TC-CHAT-02   | 대화 저장       | 저장 버튼 클릭              | `dodam_YYYYMMDD_HHMM.txt` 다운로드 |

### 9-2) 결과(예시)

| ID          | 결과   | 비고       |
| ----------- | ---- | -------- |
| TC-LOGIN-01 | Pass | 200ms 응답 |
| TC-CHAT-01  | Pass | 2.5s p95 |


### 9-3) 결과(예시)

| ID     | 결과   | 비고            |
| ------ | ---- | ------------- |
| TC-001 | Pass | 응답 450ms p95  |
| TC-010 | Pass | 메일 도착 30초 내   |
| TC-020 | Pass | 운영자 페이지 로그 확인 |


---


## 10. 향후 과제

* 푸시 알림(모바일/PWA) 정교화, 다자녀 프로필 지원
* 의료기관/약국 실시간 혼잡도·대기시간 연동
* 신뢰성 검증(출처) 자동 업데이트 및 변경 알림
* 챗봇 증강(RAG) 정답률 지표화, 금칙어/응급 가이드 보강
* 자유게시판지원
* 국가가 임산부, 아이들에게 지원하는 사업을 확인 후 국가 지원사업의 카데고리를 지원

---

## 11. 한줄 회고록
* 김민균:
* 김세한:
* 김수현:
* 정의중:
* 최우진: 이번 프로젝트는 육아 정보를 쉽고 빠르게 제공하는 챗봇 웹서비스를 만드는 것을 목표로 진행했습니다. 요구사항 정리와 설계 문서화를 꼼꼼히 진행했고, Docker와 Orion-zhen/Qwen2.5-7B-Instruct-Uncensored 모델을 활용해 챗봇의 핵심 대화 기능을 구현했습니다. 하지만 실제 구현과 운영 단계에서는 완성도나 코드 일관성이 다소 부족한 부분이 있었습니다. 이 과정을 통해 협업의 중요성과 기술 선택의 현실성, 그리고 운영까지 고려한 설계의 필요성을 깨달았습니다. 결국 좋은 설계와 기술적 도전이 있었지만, 서비스 완성도를 높이기 위해 운영 준비가 더 필요하다는 점을 느꼈습니다.
