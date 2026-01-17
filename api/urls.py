# Configurar las URLs para la API

from rest_framework.routers import DefaultRouter # Router para manejar URLs de manera automática
from .views import ItemViewSet # Importando la vista ItemViewSet para manejar operaciones CRUD en el modelo Item

# Configurando el router para manejar URLs de manera automática
router = DefaultRouter()
# Registrando la vista ItemViewSet para manejar URLs de manera automática
router.register(r'items', ItemViewSet, basename='item') 
urlpatterns = router.urls # URLs generadas por el router