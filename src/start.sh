#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
cd /usr/bin/asmp
exec gunicorn asmp.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3