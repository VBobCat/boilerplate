#!/bin/bash

echo "$SECRET_KEY" | gnome-keyring-daemon --unlock
python manage.py wait_for_database
python manage.py shell
