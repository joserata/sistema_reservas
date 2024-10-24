# reservas/views.py
from rest_framework import viewsets
from .models import Departamento, Datos, Espacios  # Asegúrate de importar ambos modelos
from .serializers import DepartamentoSerializer, DatosSerializer, EspaciosSerializer  # Asegúrate de importar ambos serializadores

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DatosViewSet(viewsets.ModelViewSet):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer

class EspaciosViewSet(viewsets.ModelViewSet):
    queryset = Espacios.objects.all()  # Obtener todos los espacios
    serializer_class = EspaciosSerializer    
