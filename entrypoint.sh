#!/bin/bash

python manage.py collectstatic --no-input

python manage.py migrate --no-input

gunicorn --bind 0.0.0.0:8000 -w 4 Dictionary.wsgi
