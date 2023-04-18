from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# TODO проверить работает ли BASE_DIR = Path.cwd()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-go5ce47%7&8k%4ic992yv&h-ph3ge-2&xam9y4s_b70=lg2&0@'

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
    # 'phonenumber_field',
    'posts.apps.PostsConfig',
    'users.apps.UsersConfig',
    'embed_video',
    'core.apps.CoreConfig',
    'sorl.thumbnail',
    'haystack',
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

# TODO переделать на PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'  # TODO изменить язык и часовой пояс

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (str(BASE_DIR / 'static'),)

# STATIC_ROOT = str(BASE_DIR / 'static') # TODO после сборки статики удалить настройку

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

POSTS_IN_PAGE = 10

LOGIN_URL = 'users:login'

LOGIN_REDIRECT_URL = 'posts:index'

MEDIA_URL = '/media/'

MEDIA_ROOT = str(BASE_DIR / 'media')

STUDENT = 'student'
TEACHER = 'teacher'
ADMIN = 'admin'
SUPERUSER = 'supeuser'  # TODO Проверить все ли роли используются
ROLES_CHOICES = [
    (STUDENT, 'Студент'),
    (TEACHER, 'Преподаватель'),
    (ADMIN, 'Администратор'),
    (SUPERUSER, 'Суперюзер Django'),
]

# AUTH_USER_MODEL = 'users.User'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# TODO удалить после разработки
INTERNAL_IPS = [
    '127.0.0.1',
]
