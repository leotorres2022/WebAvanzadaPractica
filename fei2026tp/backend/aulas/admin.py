from django.contrib import admin

from django.contrib import admin
from .models import Carrera, Profesor, Materia, Aula, ReservaAula, HorarioMateria

# Registramos cada modelo para que Django Genere el ABM automático en el Admin
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Aula)
admin.site.register(ReservaAula)
admin.site.register(HorarioMateria)
