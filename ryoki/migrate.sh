#!/bin/bash

python manage.py makemigrations blog accounts dashboard
python manage.py migrate