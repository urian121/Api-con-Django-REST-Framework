from rest_framework import viewsets # Vista para manejar operaciones CRUD en un modelo
from .models import Item # Importando el Item que está asociado el serializador
from .serializers import ItemSerializer # Importando el Serializador del modelo Item

# Usando el ModelViewSet para tener un CRUD completo en pocas líneas
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer # Serializador a utilizar para convertir objetos Item en JSON y viceversa
    filterset_fields = ['nombre', 'telefono', 'creado', 'actualizado']
    search_fields = ['nombre', 'telefono']
    ordering_fields = ['creado', 'actualizado', 'nombre']
    ordering = ['-creado']
