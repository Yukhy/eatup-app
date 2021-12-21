web: gunicorn eatup-g1t3.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate