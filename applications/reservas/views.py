# reservas/views.py
from rest_framework import viewsets
from .models import Departamento, Datos, Espacios, MetodosPago, HorariosDisponible, Roles, Usuarios, Reservas, Pagos  # Asegúrate de importar ambos modelos
from .serializers import DepartamentoSerializer, DatosSerializer, EspaciosSerializer, MetodosPagoSerializer, HorariosDisponibleSerializer, RolesSerializer, UsuariosSerializer, ReservasSerializer, PagosSerializer  # Asegúrate de importar ambos serializadores

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
    queryset = MetodosPago.objects.all() 
    serializer_class = MetodosPagoSerializer

class HorariosDisponibleViewSet(viewsets.ModelViewSet):
    queryset = HorariosDisponible.objects.all()
    serializer_class = HorariosDisponibleSerializer

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer    

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer

class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer    
