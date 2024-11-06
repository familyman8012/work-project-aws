"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "django_filters",
    "corsheaders",
    "rest_framework_simplejwt.token_blacklist",
    # Local apps
    "organizations.apps.OrganizationsConfig",
    "accounts.apps.AccountsConfig",
    "tasks.apps.TasksConfig",
    "notifications",
    "reports",
    "activities",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS 미들웨어 추가
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React 개발 서버
]
CORS_ALLOW_CREDENTIALS = True

# 운영 환경 설정
if not DEBUG:
    CORS_ALLOWED_ORIGINS = ["https://your-production-domain.com"]

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# CORS 추가 설정
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "TEST": {
            "NAME": "test_company_task_manager",
        },
    },
    "test": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_company_task_manager",
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "TEST": {
            "NAME": "test_company_task_manager",
            "MIGRATE": True,
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Company Task Manager API",
    "DESCRIPTION": "API for managing company tasks and employee workflows",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,  # /api/schema/ endpoint 직접 접근 허용
    "SWAGGER_UI_SETTINGS": {
        "persistAuthorization": True,
    },
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "SECURITY": [
        {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT token format: Bearer <token>",
            }
        }
    ],
}

# 커스텀 유저 모델 설정
AUTH_USER_MODEL = "accounts.User"

# JWT 설정 수정
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        days=7
    ),  # 액세스 토큰 15분 //개발 편의성을 위해 임시로 1일로 설정
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),  # 리프레시 토큰 1일
    "ROTATE_REFRESH_TOKENS": True,  # 리프레시 토큰 재발급
    "BLACKLIST_AFTER_ROTATION": True,  # 이전 리프레시 토큰 블랙리스트 처리
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

# CORS 설정
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True  # 개발 환경에서만!
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_HEADERS = ["*"]
    CORS_ALLOW_METHODS = ["*"]
else:
    CORS_ALLOWED_ORIGINS = ["https://your-production-domain.com"]
    CORS_ALLOW_CREDENTIALS = True

# 쿠키 설정
SESSION_COOKIE_SAMESITE = "Lax"  # None, Lax, Strict
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

if DEBUG:
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    CSRF_COOKIE_SAMESITE = None  # 개발 환경에서는 None으로 설정
    SESSION_COOKIE_SAMESITE = None
else:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# CORS 추가 설정
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
