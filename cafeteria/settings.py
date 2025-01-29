import os
from django.core.management.utils import get_random_secret_key
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = "cafeteria.urls"


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
AUTH_USER_MODEL = "authentication.CustomUser"


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",
    'drf_yasg',
    'reservations',
    'corsheaders',
    "authentication",
    "rest_framework",  
    "rest_framework.authtoken",  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "cafeteria.db",
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],   # Ensure templates folder is included
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


ALLOWED_HOSTS = ["localhost", "127.0.0.1"]  # Add more if deploying


CORS_ALLOW_ALL_ORIGINS = True  # Allow frontend requests
