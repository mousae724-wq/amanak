release: python manage.py migrate --noinput
web: python manage.py migrate --noinput && gunicorn amanak.wsgi --bind 0.0.0.0:$PORT --log-file -