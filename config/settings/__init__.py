import os


ENV = os.environ.get("DJANGO_ENV", "development")
settings_module = ""

if ENV == "production":
    settings_module = "config.settings.production"
else:
    settings_module = "config.settings.development"
