import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-go5ce47%7&8k%4ic992yv&h-ph3ge-2&xam9y4s_b70=lg2&0@'

DEBUG = True

ALLOWED_HOSTS = [
    "*",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.postgres",
    'phone_field',
    'posts.apps.PostsConfig',
    'users.apps.UsersConfig',
    'embed_video',
    'core.apps.CoreConfig',
    'sorl.thumbnail',
    'haystack',
    'ckeditor',
]

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cts.urls'

TEMPLATES_DIR = str(BASE_DIR / 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'core.context_processors.year.year'
            ],
        },
    },
]

WSGI_APPLICATION = 'cts.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', default='postgres'),
        'USER': os.getenv('POSTGRES_USER', default='postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='password'),
        'HOST': os.getenv('DB_HOST', default='db'),
        'PORT': os.getenv('DB_PORT', default='5432'),
    }
}

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = (str(BASE_DIR / 'static'),)

# STATIC_ROOT = str(BASE_DIR / 'static') # TODO после сборки статики удалить настройку

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

POSTS_IN_PAGE = 10

LOGIN_URL = 'users:login'

LOGIN_REDIRECT_URL = 'posts:index'

MEDIA_URL = '/media/'

MEDIA_ROOT = str(BASE_DIR / 'media')

STUDENT = 'student'
TEACHER = 'teacher'
ROLES_CHOICES = [
    (STUDENT, 'Студент'),
    (TEACHER, 'Преподаватель'),
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.template.context_processors.request',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'basic',
        'height': 300,
        'width': '100%',
    },
}
