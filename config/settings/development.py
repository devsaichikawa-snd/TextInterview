import os
from dotenv import load_dotenv

from .base import *


# ENV Load
load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")

# Database(SQLServer2022)
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "1433"),
        "OPTIONS": {
            "driver": os.environ.get("DRIVER"),
        },
    },
}
# Database(MySQL8.0)
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.environ.get("DB_NAME"),
#         "USER": os.environ.get("DB_USER"),
#         "PASSWORD": os.environ.get("DB_PASSWORD"),
#         "HOST": os.environ.get("DB_HOST", "localhost"),
#         "PORT": os.environ.get("DB_PORT", "3306"),
#     },
# }

# Email
EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND")
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
