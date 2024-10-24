# reservas/views.py
from rest_framework import viewsets
from .models import Departamento, Datos, Espacios, MetodosPago  # Asegúrate de importar ambos modelos
from .serializers import DepartamentoSerializer, DatosSerializer, EspaciosSerializer, MetodosPagoSerializer  # Asegúrate de importar ambos serializadores

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DatosViewSet(viewsets.ModelViewSet):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer

class EspaciosViewSet(viewsets.ModelViewSet):
    queryset = Espacios.objects.all()  # Obtener todos los espacios
    serializer_class = EspaciosSerializer    

class MetodosPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodosPago.objects.all()  # Obtener todos los métodos de pago
    serializer_class = MetodosPagoSerializer