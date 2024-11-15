# reservas/views.py
from rest_framework import viewsets
from .models import Departamento, Datos, Espacios, MetodosPago, HorariosDisponible, Roles, Usuarios, Reservas, Pagos  # Asegúrate de importar ambos modelos
from .serializers import DepartamentoSerializer, DatosSerializer, EspaciosSerializer, MetodosPagoSerializer, HorariosDisponibleSerializer, RolesSerializer, UsuariosSerializer, ReservaSerializer,  ReservasSerializer, PagosSerializer  # Asegúrate de importar ambos serializadores
from .forms import EspacioForm
from django.shortcuts import render, redirect

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
    serializer_class = ReservaSerializer  # Usa el serializador con los datos anidados


class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer    

def lista_espacios(request):
    espacios = Espacios.objects.all()
    return render(request, 'espacios/lista_espacios.html', {'espacios': espacios})

def crear_espacio(request):
    if request.method == 'POST':
        form = EspacioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_espacios')  # Redirige a la lista después de crear el espacio
    else:
        form = EspacioForm()
    return render(request, 'espacios/crear_espacio.html', {'form': form})