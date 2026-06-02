from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mostrar = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Materia(models.Model):
    nombre = models.CharField(max_length=128)
    cant_alumnos = models.IntegerField(default=5)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='materias')
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return self.nombre


class Aula(models.Model):
    descripcion = models.CharField(max_length=128)
    ubicacion = models.CharField(max_length=128) # Nota: evitamos la 'ó' con tilde en el nombre de la variable
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion
    
class ReservaAula(models.Model):
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='reservas')
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    observacion = models.CharField(max_length=256)

    def __str__(self):
        return f"Reserva Aula {self.id_aula_id} ({self.fh_desde} - {self.fh_hasta})"


class HorarioMateria(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='horarios')
    id_reserva = models.ForeignKey(ReservaAula, on_delete=models.CASCADE, related_name='horarios')
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()

    def __str__(self):
        return f"Horario Materia {self.id_materia_id} ({self.fh_desde})"
