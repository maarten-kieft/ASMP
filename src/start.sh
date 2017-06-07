echo "Copying initial database if not exists"
cp -n /usr/bin/asmp/db.sqlite3 /usr/bin/asmp/db.sqlite3

echo "Executing database migrations"
python3 manage.py migrate

# Start Gunicorn processes
echo "Starting Website"
cd /usr/bin/asmp
gunicorn asmp.wsgi:application --bind 0.0.0.0:8000 --workers 3 --daemon
    
# Start nginx
echo "Stating nginx"
service nginx start

# Start the worker
echo "Starting Worker"
python3 manage.py worker