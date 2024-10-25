from rest_framework import serializers
from .models import Departamento, Datos, Espacios, MetodosPago, HorariosDisponible, Roles, Usuarios, Reservas, Pagos


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos  # Especifica el modelo que estás serializando
        fields = '__all__'  # Incluye todos los campos del modelo

class EspaciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacios
        fields = '__all__'

class MetodosPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodosPago
        fields = '__all__'        

class HorariosDisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorariosDisponible
        fields = '__all__'        

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__' 

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'