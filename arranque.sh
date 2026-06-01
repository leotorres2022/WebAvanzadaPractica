#!/bin/bash
set -e

echo "--> Verificando si existe el proyecto Django..."

if [ ! -f "manage.py" ]; then
    echo "--> No se encontró un proyecto Django. Creando proyecto vacío..."
    django-admin startproject core .
fi

echo "--> Generando y aplicando migraciones de Base de Datos..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "--> Creando superusuario (si no existe)..."

python manage.py createsuperuser --noinput || echo "--> El superusuario ya existe o no se pudo crear."

echo "--> Arrancando el servidor de desarrollo de Django en el puerto 8000..."
exec python manage.py runserver 0.0.0.0:8000