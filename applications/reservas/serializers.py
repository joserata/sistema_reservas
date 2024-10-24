from rest_framework import serializers
from .models import Departamento, Datos, Espacios, MetodosPago

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