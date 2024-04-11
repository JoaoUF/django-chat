from .base import *

DEBUG = bool(os.environ.get('DEGUB'))
# DEBUG = True
PRODUCTION = os.environ.get('PRODUCTION')
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
WSGI_APPLICATION = 'core.wsgi.development.application'
ASGI_APPLICATION = 'core.asgi.development.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfields')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafields')
