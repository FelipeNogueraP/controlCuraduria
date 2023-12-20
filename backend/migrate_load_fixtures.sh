#!/bin/bash

# Navigate to the Django project directory (if not already there)
cd /app

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Load all fixtures from the fixtures directory
# Adjust the path to your fixtures directory as needed
for fixture in control_app/fixtures/*.json; do
    echo "Loading fixture: $fixture"
    python manage.py loaddata "$fixture"
done