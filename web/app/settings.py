"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see./
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os
from django.utils.translation import ugettext_lazy as _
from kombu import Exchange, Queue

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '[]')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "app/templates"),
)
# Application definition

INSTALLED_APPS = [
    # 'djangocms_admin_style',

    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Thered part apps
    'cms',
    'sekizai',
    'parler',
    'menus',
    'treebeard',
    'rest_framework',
    'rest_framework_swagger',
    'djangocms_text_ckeditor',
    'django_filters',
    'rest_framework_filters',
    'adminsortable2',
    'multimenus',

    'easy_thumbnails',
    'filer',
    'mptt',
    'webpack_loader',
    # 'debug_toolbar',

    # Apps
    'apps.core',
]

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'libraries': {
            },
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("REDIS_HOST", "redis://redis:6379/0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    },
    'translations_cache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'HOST': os.environ.get('DB_SERVICE', ''),
        'PORT': os.environ.get('DB_PORT', '')
    }
}

# Celery settings

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_FROM = os.environ.get('EMAIL_FROM', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', 'False') == 'True'

# i18
LANGUAGE_CODE = 'ru'

USE_I18N = True
LANGUAGES = (
    ('ru', _('Русский')),
    ('en', _('English')),
)

PARLER_LANGUAGES = {
    1: (
        {'code': 'ru', },
        {'code': 'en', },
    )
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

DATE_FORMAT = "d-m-Y"
USE_L10N = False

ADMIN_ENABLED = os.environ.get('ADMIN_ENABLED', 'False') == 'True'
CMS_TEMPLATES = (
    ('layouts/base/layout_base.html', 'Базовый шаблон'),
    ('layouts/base/layout_index.html', 'Шаблон главной страницы'),
    ('layouts/base/layout_with_ticker.html', 'Шаблон c бегущей строкой'),
)

SITE_ID = 1

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'assets/dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'app/webpack-stats-live.json' if not DEBUG else 'app/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

if DEBUG:
    CMS_PAGE_CACHE = False
    CMS_PLACEHOLDER_CACHE = False
    CMS_PLUGIN_CACHE = False

REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'apps.core.authentication.XTokenAuthentication',
    # ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.core.authentication.XTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_filters.backends.RestFrameworkFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}
TIME_ZONE = 'Europe/Moscow'

RADIO_CO_URL = 'https://s3.radio.co/s1f26345be/listen'

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'forcePasteAsPlainText': 'true',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['Bold', 'Italic', 'TextColor', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['Format', 'NumberedList', 'BulletedList', '-', 'Link', 'Unlink', '-', 'RemoveFormat'],
        ['Source', 'ShowBlocks']
    ],
    'format_tags': 'p;h2;h3;div',
}

CKEDITOR_SETTINGS_MIN = {
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['Bold', 'Italic', 'Underline'],
        ['RemoveFormat']
    ]
}

CKEDITOR_SETTINGS_MIN_WITH_LINKS = {
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['Bold', 'Italic', 'Underline'],
        ['RemoveFormat'],
        [ 'Link', 'Unlink', 'Anchor' ],
    ]
}

CKEDITOR_SETTINGS_HIGHLIGHT = {
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['TextColor', 'BGColor'],
        ['RemoveFormat']
        # ['Bold', 'Italic', 'Underline'],
    ]
}

FILE_UPLOAD_PERMISSIONS = 0o644

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return DEBUG


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
