#!/bin/bash

echo "Copying initial database if not exists"
cp -n /usr/bin/asmp/db.sqlite3 /usr/bin/asmp/db.sqlite3

# Start Gunicorn processes
echo "Starting Website"
cd /usr/bin/asmp
gunicorn asmp.wsgi:application \
    --workers 3 \
	--daemon \
    --bind unix:/usr/bin/asmp/gunicorn.sock \
	
# Start the worker
echo "Starting Worker"
python3 manage.py worker

# Start nginx
service nginx start