release: python manage.py migrate --noinput
web: gunicorn amanak.wsgi --bind 0.0.0.0:$PORT --log-file -