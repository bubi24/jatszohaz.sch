#!/bin/bash
set -o errexit
set -o xtrace

git clone https://github.com/nyirit/jatszohaz.sch.git

source jh/bin/activate

cd jatszohaz.sch
pip install -r requirements.txt --upgrade

cd jatszohaz
python3 manage.py migrate
python3 manage.py collectstatic --no-input --clear
python3 manage.py compilemessages

gunicorn \
    jatszohaz.wsgi:application \
    --bind 0.0.0.0:8000
