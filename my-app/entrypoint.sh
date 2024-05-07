#!/bin/ash

echo "Apply database migrations"
python manage.py migrate

echo "Starting Django server on port $PORT"
python manage.py runserver 0.0.0.0:$PORT

exec "$@" 
