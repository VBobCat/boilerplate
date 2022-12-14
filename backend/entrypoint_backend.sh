#!/bin/bash

python manage.py collectstatic --noinput
python manage.py wait_for_database
python manage.py migrate
