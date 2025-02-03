"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
with open(BASE_DIR / '.secret_config'/'secret.json') as f:
    config_secret_str = f.read()

SECRET = json.loads(config_secret_str)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'todo',
    'users',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'django_summernote',
    'django_cleanup',
]

INSTALLED_APPS = INSTALLED_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_DIR = BASE_DIR / 'static'

STATICFILES_DIRS = [
    STATIC_DIR,
]

STATIC_ROOT = BASE_DIR / '.static_root'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# login / logout
LOGIN_REDIRECT_URL = '/cbv/todo/' # 로그인 후에 To Do List 페이지로 이동하기 위함
LOGOUT_REDIRECT_URL = '/accounts/login/' # 로그아웃 시 로그인 페이지로 이동하기 위함

# Summernote 설정
SUMMERNOTE_CONFIG = {
    # HTML 태그 또는 JS를 수정하지 못하도록 iframe 설정
    'iframe': True,

    'summernote': {
        # airMode 비활성화: 툴바를 항상 표시하도록 설정
        'airMode': False,

        # 에디터의 사이즈 정의
        'width': '100%',    # 에디터의 너비를 100%로 설정
        'height': '480',    # 에디터의 높이를 480px로 설정

        # 에디터의 툴바 메뉴 정의
        'toolbar': [
            ['style', ['style']],                      # 스타일 설정
            ['font', ['bold', 'underline', 'clear']],  # 글꼴 설정: 굵게, 밑줄, 지우기
            ['color', ['color']],                      # 색상 설정
            ['para', ['ul', 'ol', 'paragraph']],       # 문단 설정: 글머리 기호, 번호 매기기, 문단
            ['table', ['table']],                      # 표 삽입
            ['insert', ['link', 'picture']],           # 삽입 기능: 링크, 그림
            ['view', ['fullscreen']],                  # 보기 설정: 전체 화면
        ],

        # 에디터 언어 정의
        'lang': 'ko-KR',  # 에디터의 언어를 한국어로 설정

        # 코드미러 설정
        'codemirror': {
            'mode': 'htmlmixed',     # 코드미러의 모드를 htmlmixed로 설정
            'lineNumbers': 'true',   # 코드미러에서 줄 번호를 표시
            'theme': 'monokai',      # 코드미러의 테마를 monokai로 설정
        },
    },

    # 첨부파일 인증 필요 여부 설정
    'attachment_require_authentication': True,

    # 첨부파일 기능 비활성화 설정
    'disable_attachment': False,

    # 첨부파일의 절대경로 URI 사용 설정
    'attachment_absolute_uri': True,
}
# auth
AUTH_USER_MODEL = 'users.User'

# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.naver.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = SECRET['EMAIL']['USER']
EMAIL_HOST_PASSWORD = SECRET['EMAIL']['PASSWORD']
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER