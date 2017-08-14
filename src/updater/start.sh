#!/bin/bash
echo "Copying initial database if not exists"
cp -n /usr/bin/asmp/db.sqlite3 /usr/bin/asmp/db.sqlite3
cd /usr/bin/asmp

echo "Executing database migrations"
python3 manage.py migrate

echo "Starting Updater"
python3 manage.py runupdater