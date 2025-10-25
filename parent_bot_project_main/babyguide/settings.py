# babyguide/settings.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Required core settings ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-me')  # 기본값 추가
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ["13.124.52.49", "localhost", "127.0.0.1"]  # 127.0.0.1 추가

INSTALLED_APPS = [
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes',
    'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles',
    'core',  # 추가
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise 추가 (SecurityMiddleware 바로 다음)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # 템플릿 루트
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'babyguide.urls'
WSGI_APPLICATION = 'babyguide.wsgi.application'

# Database 설정 - 환경 변수 필수
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# WhiteNoise 설정 (압축 및 캐싱)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- i18n / timezone ---
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

# --- Model defaults ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Email 설정 ---
# 이메일 백엔드 설정 (SMTP 사용 시 실제 메일 발송, console은 터미널 출력)
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

# SMTP 서버 주소 (Gmail: smtp.gmail.com, Naver: smtp.naver.com)
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')

# SMTP 포트 번호 (587: TLS, 465: SSL)
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))

# TLS 암호화 사용 여부 (True 권장)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'

# 발송용 이메일 주소
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')

# 이메일 계정 비밀번호 (Gmail은 앱 비밀번호 사용)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# 기본 발신자 이메일 주소
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'no-reply@babyguide.local')