from rest_framework import routers
from .viewsets import ClientesViewSet

router = routers.SimpleRouter()

router.register('Clientes', ClientesViewSet)


urlpatterns = router.urls