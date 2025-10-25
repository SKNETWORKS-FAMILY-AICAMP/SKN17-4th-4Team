-- 처음 한번만
✅ 	1.	가상환경 생성
conda create -n django python=3.12

✅ 	2. 프로젝트 생성
pip install django
django-admin startproject babyguide .
python manage.py startapp core

✅ 	3. 디비 및 테이블 생성
CREATE DATABASE babyguide CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

✅ 	4. Python용 MySQL 드라이버 설치 (Windows)
conda activate django
pip install mysqlclient

# mysqlclient 설치 실패 시 PyMySQL 대체 사용
# pip install pymysql
# 그 후 babyguide/settings.py 최상단에 추가:
# import pymysql
# pymysql.install_as_MySQLdb()

✅ 	5. babyguide/settings.py에 MySQL 연결 설정
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'babyguide',         # 위에서 만든 DB 이름
        'USER': 'root',              # DB 사용자명
        'PASSWORD': 'root',        # DB 비밀번호
        'HOST': 'localhost',         # 로컬이면 그대로
        'PORT': '3306',              # MySQL 기본 포트
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

✅ 	6. 마이그레이션 다시 적용
python manage.py migrate




-- 계속
✅ 	1.	마이그레이션 초기화
conda activate django
python manage.py migrate

✅ 	2.	서버 실행
python manage.py runserver
