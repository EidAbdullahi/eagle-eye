

"""
Django settings for Eagle Eye Security Service
Optimized for development + cPanel production deployment
Uses MySQL, WhiteNoise for static files, and Cloudinary for media.
"""

import os
from pathlib import Path
from decouple import config
import pymysql
from django.db.backends.mysql.base import DatabaseWrapper

# ============================================================================
# MySQL / MariaDB compatibility
# ============================================================================
DatabaseWrapper.mysql_is_mariadb = property(lambda self: False)
pymysql.install_as_MySQLdb()

# ============================================================================
# Paths
# ============================================================================
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# ============================================================================
# Security
# ============================================================================

SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-change-me"
)

DEBUG = config(
    "DEBUG",
    default=True,
    cast=bool
)



if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='eagleyesecurityservice.com,www.eagleyesecurityservice.com').split(',')

# ============================================================================
# Applications
# ============================================================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # Project apps
    "myapp",

    # Cloudinary
    "cloudinary",
    "cloudinary_storage",

    # Dev tools
    "django_extensions",
]

# ============================================================================
# Middleware
# ============================================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ============================================================================
# URLs
# ============================================================================
ROOT_URLCONF = "myproject.urls"

WSGI_APPLICATION = "myproject.wsgi.application"

# ============================================================================
# Templates
# ============================================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# ============================================================================
# Database
# ============================================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME", default="eagle_eye_db"),
        "USER": config("DB_USER", default="root"),
        "PASSWORD": config("DB_PASSWORD", default=""),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="3306"),
    }
}

# ============================================================================
# Password validation
# ============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

# ============================================================================
# Internationalization
# ============================================================================
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# ============================================================================
# Static files
# ============================================================================
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ============================================================================
# Media files
# ============================================================================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ============================================================================
# Cloudinary
# ============================================================================
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": config("CLOUDINARY_CLOUD_NAME", default=""),
    "API_KEY": config("CLOUDINARY_API_KEY", default=""),
    "API_SECRET": config("CLOUDINARY_API_SECRET", default=""),
    "SECURE": True,
}

DEFAULT_FILE_STORAGE = (
    "cloudinary_storage.storage.MediaCloudinaryStorage"
    if config("CLOUDINARY_CLOUD_NAME", default="")
    else "django.core.files.storage.FileSystemStorage"
)

# ============================================================================
# Default primary key
# ============================================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ============================================================================
# Security settings
# ============================================================================

if DEBUG:

    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False

else:

    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# ============================================================================
# About Images
# ============================================================================

ABOUT_IMAGES_URL = "/about_images/"
ABOUT_IMAGES_ROOT = BASE_DIR / "about_images"