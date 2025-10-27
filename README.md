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
- [10. 수행 결과](#10-수행-결과)
- [11. 향후 과제](#11-향후-과제)
- [12. 한줄 회고록](#12-한줄-회고록)

---

## 1. 👨‍👩‍👧‍👦 팀 소개

<h2>육아 복지부</h2>

<table align="center">
  <tr>
    <td align="center" valign="top" style="padding: 10px;">
      <strong>김민균</strong><br/>
      <img src="https://github.com/user-attachments/assets/b242f6f7-423a-441f-9fed-65e754f4aa93" width="150" alt="김민균"/>
    </td>
    <td align="center" valign="top" style="padding: 10px;">
      <strong>김세한</strong><br/>
      <img src="https://github.com/user-attachments/assets/565cf252-2433-4bcb-9c82-1bbd35e42d8a" width="150" alt="김세한"/>
    </td>
    <td align="center" valign="top" style="padding: 10px;">
      <strong>김수현</strong><br/>
      <img src="https://github.com/user-attachments/assets/b3101204-db35-48ed-823c-66e9e441ccba" width="150" alt="김수현"/>
    </td>
    <td align="center" valign="top" style="padding: 10px;">
      <strong>정의중</strong><br/>
      <img src="https://github.com/user-attachments/assets/c0790bf8-cc79-4e38-b0d1-b49a27eadbab" width="150" alt="정의중"/>
    </td>
    <td align="center" valign="top" style="padding: 10px;">
      <strong>최우진</strong><br/>
      <img src="https://github.com/user-attachments/assets/d8451ecc-a69e-46ec-b00f-dbd2eefec6e0" width="150" alt="최우진"/>
    </td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/alswhitetiger">@alswhitetiger</a></td>
    <td align="center"><a href="https://github.com/kimsehan11">@kimsehan11</a></td>
    <td align="center"><a href="https://github.com/K-SH98">@K-SH98</a></td>
    <td align="center"><a href="https://github.com/uii42">@uii42</a></td>
    <td align="center"><a href="https://github.com/CHUH00">@CHUH00</a></td>
  </tr>
</table>

<br><br/>

<br>




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

<img width="1641" height="479" alt="image" src="https://github.com/user-attachments/assets/c5080a65-dbca-4bd3-a854-0b8f134f5b19" />

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
<img width="1536" height="1024" alt="12" src="https://github.com/user-attachments/assets/8bcb62da-e5a7-4a8a-834b-498cdba33ed4" />


---

## 6. 핵심 기능

* **도담이 챗봇**: 자연어 질의에 대한 요약형 답변, 출처/갱신일 표기, 최근 대화 **.txt 저장**
* **인증**: 이메일 로그인/회원가입(닉네임/이메일/비밀번호 규칙/인증번호)
* **홈 랜딩**: 서비스 소개, 챗봇 시작 CTA, 푸터(운영사/저작권)

---

## 7. 요구사항 정의

<img width="1287" height="781" alt="image" src="https://github.com/user-attachments/assets/05bb3611-5bb1-4d82-bbef-b4e04a756afe" />



---

## 8. 화면 설계서

### 8-1) 메인 홈 화면 (`scr-home-01`)

<img width="1382" height="792" alt="image" src="https://github.com/user-attachments/assets/3c79a46e-7033-4441-945b-f6fe218e1587" />




---

### 8-2) 로그인 화면 (`scr-user-01`)

<img width="1381" height="789" alt="image" src="https://github.com/user-attachments/assets/75e9b0ad-3265-4e93-812c-5f3e0f111cbd" />




---

### 8-3) 회원가입 화면 (`scr-user-02`)

<img width="1390" height="795" alt="image" src="https://github.com/user-attachments/assets/a0bb3f7b-e31c-4fc7-8e7f-fdf1ca5e161b" />




---

### 8-4) 챗봇 화면 (`scr-chat-01`)

<img width="1393" height="794" alt="image" src="https://github.com/user-attachments/assets/997c13ba-11ff-41db-b2cb-790d632fd11a" />



---

## 9. 테스트 계획 및 결과

### 9-1) 테스트 계획

| ID           | 시나리오        | 절차                    | 기대 결과                          |
| ------------ | ----------- | --------------------- | ------------------------------ |
| test-01  | 이메일 로그인 성공  | 올바른 계정 입력 → 로그인       | 홈 이동, 세션 생성                    |
| test-02  | 이메일 로그인 실패  | 잘못된 비밀번호 입력           | 오류 팝업창 노출                 |
| test-03 | 인증 메일 발송/검증 | 이메일 입력 → 인증요청 → 코드 입력 | 1분 내 메일 수신·검증 통과               |
| test-04   | 기본 질의/응답    | 질문 입력 → 응답 확인         | 답변 표시                |
| test-05   | 대화 저장       | 저장 버튼 클릭              | `.txt` 다운로드 |

### 9-2) 결과

| ID          | 결과   | 비고       |
| ----------- | ---- | -------- |
| test-01 | Pass | 홈 이동 완료 |
| test-02  | Pass | 팝업창 노출 완료 |
| test-03 | Pass |  1분 내 메일 수신 완료 |
| test-04 | Pass |  답변 표시 완료  |
| test-05 | Pass | .txt 다운로드 완료 |


---
## 10. 수행 결과
<img width="1919" height="963" alt="12" src="https://github.com/user-attachments/assets/99cc66a7-d4e3-40e4-9736-7e6ea4c2b06c" />

<img width="1587" height="472" alt="31" src="https://github.com/user-attachments/assets/77078312-ec70-495a-bd5a-c54f12b38590" />

<img width="1573" height="839" alt="1444" src="https://github.com/user-attachments/assets/3cad2611-56db-4b2c-98ab-03ad8ee9b208" />


---

## 11. 향후 과제

* 푸시 알림(모바일/PWA) 정교화, 다자녀 프로필 지원
* 의료기관/약국 실시간 혼잡도·대기시간 연동
* 신뢰성 검증(출처) 자동 업데이트 및 변경 알림
* 챗봇 증강(RAG) 정답률 지표화, 금칙어/응급 가이드 보강
* 자유게시판지원
* 국가가 임산부, 아이들에게 지원하는 사업을 확인 후 국가 지원사업의 카데고리를 지원

---

## 12. 한줄 회고록
* 김민균: 프로젝트에서 피그마 등을 새롭게 접하게 되었고, AWS 등을 처음 하게 되면서 어려운 것도 많이 있었고 시간이 부족해서 이번 프로젝트에서 추가하고 싶었지만 못 했던 부분들이 너무 아쉽게 느껴졌습니다. 다음에는 조금 더 노력해서 부족한 부분을 채워 프로젝트를 좀 더 완벽하게 만들고 싶습니다
* 김세한: 이번 프로젝트를 통해 AWS 배포를 직접 구성하고 Docker로 서비스와 의존성을 컨테이너화했으며, RunPod GPU의 FastAPI 엔드포인트를 EC2(또는 리버스 프록시)와 안전하게 연동하는 법을 익혔고, 프런트에서는 HTML·CSS·JavaScript로 구조·스타일·동작을 분리하고 비동기 API 호출 흐름까지 이해해 전체 흐름을 한눈에 잡을 수 있었다.
* 김수현: Figma를 처음 사용해 어려움이 있었지만, 디자인을 구현하는 과정이 흥미로웠습니다. 시간상 기능적으로 할 수 있는 부분이 적어 아쉬움이 많이 남아 추후에 배포까지 완성하는 웹 개발에 도전하고 싶다는 목표가 생겼습니다.
* 정의중:이번 프로젝트에서 저는 기획 전반과 FastAPI를 활용한 RunPod 연동을 담당했습니다.
프로젝트를 진행하며 사용자의 관점에서 서비스 구조를 설계하고, 실제로 동작 가능한 형태로 구현하는 것의 중요성을 배웠습니다.
* 최우진: 이번 프로젝트는 육아 정보를 쉽고 빠르게 제공하는 챗봇 웹서비스를 만드는 것을 목표로 진행했습니다. 요구사항 정리와 설계 문서화를 꼼꼼히 진행했고, Docker와 Orion-zhen/Qwen2.5-7B-Instruct-Uncensored 모델을 활용해 챗봇의 핵심 대화 기능을 구현했습니다. 하지만 실제 구현과 운영 단계에서는 완성도나 코드 일관성이 다소 부족한 부분이 있었습니다. 이 과정을 통해 협업의 중요성과 기술 선택의 현실성, 그리고 운영까지 고려한 설계의 필요성을 깨달았습니다. 결국 좋은 설계와 기술적 도전이 있었지만, 서비스 완성도를 높이기 위해 운영 준비가 더 필요하다는 점을 느꼈습니다.
