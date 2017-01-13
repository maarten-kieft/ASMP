#!/bin/bash

# Copy initial database if not exists
echo "Init database file"
cp -n /usr/bin/asmp/db.sqlite3 /usr/bin/asmp/data/db.sqlite3

# Start Gunicorn processes
echo "Starting Website"
cd /usr/bin/asmp
gunicorn asmp.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
	--daemon
	
# Start the worker
echo "Starting Worker"
python manage.py worker