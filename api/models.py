from django.db import models

# Modelo para representar un ítem en la lista
class Item(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    # Método para representar el objeto como una cadena
    def __str__(self):
        return f"{self.nombre} - {self.telefono}"
    
    # Meta clase para configurar el modelo
    class Meta:
        db_table = 'items'
        ordering = ['creado']
