#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser('admin','andressrojasr@gmail.com','admin')
python manage.py djangorestframework_simplejwt create_keys