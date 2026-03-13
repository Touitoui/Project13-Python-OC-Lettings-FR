#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); username='${DJANGO_SUPERUSER_USERNAME}'; email='${DJANGO_SUPERUSER_EMAIL}'; password='${DJANGO_SUPERUSER_PASSWORD}'; User.objects.filter(username=username).exists() or User.objects.create_superuser(username, email, password)"
fi

exec gunicorn --bind 0.0.0.0:8000 --workers 3 oc_lettings_site.wsgi:application
