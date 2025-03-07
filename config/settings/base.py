import os
from pathlib import Path
from django.contrib.messages import constants as message_constants


# Directory Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Application definition
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps",
]

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

ROOT_URLCONF = "config.urls"

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
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# Internationalization
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# AUTH
AUTH_USER_MODEL = "apps.User"
LOGIN_URL = "/textinterview/login/"
LOGOUT_URL = "/textinterview/logout/"
LOGIN_REDIRECT_URL = "/textinterview/login/"
LOGOUT_REDIRECT_URL = "/textinterview/login/"
SESSION_COOKIE_AGE = 86400  # セッション有効期限:1日間
SESSION_SAVE_EVERY_REQUEST = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# message
MESSAGE_TAGS = {
    message_constants.DEBUG: "debug",
    message_constants.INFO: "info",
    message_constants.SUCCESS: "success",
    message_constants.WARNING: "warning",
    message_constants.ERROR: "error",
}

# ログ設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(asctime)s %(filename)s %(module)s %(message)s",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
            "formatter": "simple",
        },
        "file": {
            "level": "ERROR",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "backupCount": 12,
            "encoding": "utf-8",
            "delay": True,
            "filename": os.path.join(LOG_DIR, "error.log"),
            "filters": [],
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": True,
        },
    },
}
