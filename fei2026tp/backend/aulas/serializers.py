from rest_framework import models, serializers
from .models import Carrera, Profesor, Materia, Aula, ReservaAula, HorarioMateria

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'


class ReservaAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAula
        fields = '__all__'


class HorarioMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioMateria
        fields = '__all__'