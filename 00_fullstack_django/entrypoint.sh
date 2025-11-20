#!/bin/sh

if [ "DATABASE" = "postgres" ]
then
    echo "Wating for postgres..."

    # TODO: setup Host and Port 
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL is avialable"
fi

python manage.py migrate

exec "$@"
