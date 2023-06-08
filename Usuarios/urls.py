from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/Usuarios',UsuariosViewSet, 'usuarios')
router.register('api/RegUsuarios',RegUsuariosViewSet, 'RegUsuarios')
router.register('api/RegAlimentos',RegistroAlimentosViewSet, 'RegAlimentos')
router.register('api/TipAlimentos',TipAlimentosViewSet, 'TipAlimentos')
router.register('api/Alimentos',AlimentosViewSet, 'Alimentos')
router.register('api/DetAlimentos',DetalleAlimentosViewSet, 'DetAlimentos')
router.register('api/Administradores', AdministradoresViewSet,'Administradores')

urlpatterns = router.urls