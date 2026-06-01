#!/bin/bash

echo "--> Ejecutando Python dentro del contenedor"
docker compose exec django python "$@"
chmod +x bin/python.sh
