"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

from django.urls import reverse_lazy


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x4m_+7v@^gojy#x6s#l7&^3f5r^6j1s(wmyx6ot&@6cnpyf7c('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'account.User'
# Application definition

INSTALLED_APPS = [
    'jet',
    'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    # my apps
    'about',
    'account',
    'blog',
    'contact',
    'home',
    'pages',
    'shop',
    'vendor',
    'social_django',
    'django_celery_beat',
    'taggit',
]


AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           'social_core.backends.facebook.FacebookOAuth2',
                           'social_core.backends.google.GoogleOAuth2',
]


# [...]

LOGIN_URL = reverse_lazy('account:login')
LOGIN_REDIRECT_URL = reverse_lazy('home:home')
LOGOUT_URL = reverse_lazy('account:logout')
LOGOUT_REDIRECT_URL = reverse_lazy('account:login')

# [...]


#[...]

SOCIAL_AUTH_FACEBOOK_KEY = '482741373256989'        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '74557900294f5bd99200e45b08d14d7a' # App Secret


SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '96253623111-1hri97dnv1glth49i901jos51m9efoch.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_friends']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields' : 'id,name,email,picture'
}
#[...]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',  # <--
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # multi language
                'social_django.context_processors.backends',  # social auth
                'social_django.context_processors.login_redirect', # social auth
                'django.template.context_processors.request',# jet
                'shop.contex_processors.global_product_category'
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.8'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

\

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('az', ugettext('Azerbaijan')),

)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "",'locale/'),
)





JET_DEFAULT_THEME = 'green'
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]







# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mammadovhuseyn37@gmail.com'
EMAIL_HOST_PASSWORD = 'ndagnhossxdqavle'


DEFAULT_FROM_EMAIL = 'mammadovhuseyn37@gmail.com'






CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Baku'

SITE_ADDRESS = 'http://localhost:8000'
