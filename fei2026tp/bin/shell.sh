#!/bin/bash

echo "--> Entrando al Shell en el contenedor de Django..."
docker compose exec django python manage.py shell