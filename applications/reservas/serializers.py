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

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id_usuario', 'nombre']  # Ajusta según el campo que contiene el nombre del usuario

class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacios
        fields = ['id', 'name']  # Ajusta si el campo del nombre es distinto
        
class ReservaSerializer(serializers.ModelSerializer):
    id_usuario = UsuarioSerializer()
    id_espacio = EspacioSerializer()

    # Se aseguran de que se serialicen correctamente los tipos de datos de fecha y hora
    fecha_reserva = serializers.DateField()  # Para el campo solo de fecha
    hora_inicio = serializers.TimeField()  # Para el campo solo de hora
    hora_fin = serializers.TimeField()  # Para el campo solo de hora
    fecha_creacion = serializers.DateTimeField()  # Para el campo timestamp

    class Meta:
        model = Reservas
        fields = ['id_reserva', 'id_usuario', 'id_espacio', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'estado', 'comentarios', 'fecha_creacion']