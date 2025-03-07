python manage.py collectstatic --noinput
gunicorn --workers 3 --bind 0.0.0.0:8000 --timeout 600 config.wsgi:application
