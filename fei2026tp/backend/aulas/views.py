from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Carrera
from .serializers import CarreraSerializer
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Profesor
from .serializers import ProfesorSerializer

class CarreraMixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

    # Mapeamos el método HTTP GET a la función list del ListModelMixin
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Mapeamos el método HTTP POST a la función create del CreateModelMixin
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class ProfesorMixinDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    # Obtener un profesor específico por ID (GET)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Modificar un profesor específico por ID (PUT/PATCH)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # Eliminar un profesor específico por ID (DELETE)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    

