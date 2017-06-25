#!/bin/bash
echo "Copying initial database if not exists"
cp -n /usr/bin/asmp/db.sqlite3 /usr/bin/asmp/db.sqlite3
cd /usr/bin/asmp

echo "Executing database migrations"
python3 manage.py migrate

# Start Gunicorn processes
echo "Starting Website"
gunicorn asmp.wsgi:application --bind 0.0.0.0:8000 --workers 3 --daemon
    
# Start nginx
echo "Stating nginx"
service nginx start


# Start the aggregator
echo "Starting Aggregator"
python3 manage.py runaggregator &

# Start the worker
echo "Starting Processor"
python3 manage.py runprocessor