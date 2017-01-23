#!/bin/bash

# Start Gunicorn processes
echo "Starting Website"
cd /usr/bin/asmp
gunicorn asmp.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
	--daemon
	
# Start the worker
echo "Starting Worker"
python3 manage.py worker