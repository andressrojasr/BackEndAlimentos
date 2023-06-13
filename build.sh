#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py makemigrations
echo "
from django.contrib.auth import get_user_model; 
User = get_user_model(); 
User.objects.create_superuser('andres', 'aramirez7310@uta.edu.ec', 'andres')
" | python manage.py shell