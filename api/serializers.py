# Serializador para el modelo Item , convierte objetos Item en representaciones JSON y viceversa
from rest_framework import serializers
from .models import Item

# Serializador para el modelo Item)
class ItemSerializer(serializers.ModelSerializer):
    # Meta clase para configurar el serializador
    class Meta:
        model = Item # Modelo al que está asociado el serializador
        fields = ['id', 'nombre', 'telefono', 'creado', 'actualizado'] # Campos del modelo a serializar
        read_only_fields = ['id', 'creado', 'actualizado'] # Campos que solo se pueden leer, no escribir
        # fields = '__all__' # Incluir todos los campos del modelo en el serializador