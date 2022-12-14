#!/bin/bash

python manage.py wait_for_database
gunicorn backend.wsgi:application \
         --bind 0.0.0.0:8000
