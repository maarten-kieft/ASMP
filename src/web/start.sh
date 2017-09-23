#!/bin/bash
cd /usr/bin/asmp

echo "Stating nginx"
service nginx start

echo "Starting Website"
gunicorn asmp.wsgi:application --bind 0.0.0.0:8000 --workers 3