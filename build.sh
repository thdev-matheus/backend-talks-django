#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install --upgrade pip

python manage.py migrate
python manage.py loaddata fixture.json