from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Carrera
from .serializers import CarreraSerializer

class CarreraMixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

    # Mapeamos el método HTTP GET a la función list del ListModelMixin
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Mapeamos el método HTTP POST a la función create del CreateModelMixin
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

