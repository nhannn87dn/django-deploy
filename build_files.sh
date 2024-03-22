#!/usr/bin/env bash
# exit on error
set -o errexit

echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput --clear
echo "BUILD END"