from rest_framework import routers
from .api import *
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()

router.register('Usuarios',UsuariosViewSet, 'usuarios')
router.register('RegUsuarios',RegUsuariosViewSet, 'RegUsuarios')
router.register('RegAlimentos',RegistroAlimentosViewSet, 'RegAlimentos')
router.register('TipAlimentos',TipAlimentosViewSet, 'TipAlimentos')
router.register('Alimentos',AlimentosViewSet, 'Alimentos')
router.register('DetAlimentos',DetalleAlimentosViewSet, 'DetAlimentos')

urlpatterns = [
    path('auth/loginView/', LoginView.as_view(), name='loginView'),
    path('auth/existeRegistro/', ExisteRegistro.as_view(), name='existeRegistro'),
    path('auth/insertarRegistro/', InsertarRegistro.as_view(), name='insertarRegistro'),
    path('auth/listarRegistros/', listarRegistros.as_view(), name='listarRegistros'),
    path('auth/editarRegistro/', editarRegistro.as_view(), name='editarRegistro'),
    path('auth/eliminarRegistro/', eliminarRegistro.as_view(), name='eliminarRegistro'),
    path('auth/filtrarRegistro/', filtrarRegistro.as_view(), name='filtrarRegistro'),
    path('auth/insertarRegistroAlimentos/', insertarRegistroAlimentos.as_view(), name='insertarRegistroAlimentos'),
    path('auth/listarRegistrosAlimentos/', listarRegistrosAlimentos.as_view(), name='listarRegistrosAlimentos'),
    path('auth/filtrarRegistrosAlimentos/', filtrarRegistrosAlimentos.as_view(), name='filtrarRegistrosAlimentos'),
    path('auth/listarTiposDeAlimentos/', listarTiposDeAlimentos.as_view(), name='listarTiposDeAlimentos'),
    path('auth/listarAlimentos/', listarAlimentos.as_view(), name='listarAlimentos'),
    path('auth/editarRegistroAlimentos/', editarRegistroAlimentos.as_view(), name='editarRegistroAlimentos'),
    path('auth/eliminarRegistroAlimentos/', eliminarRegistroAlimentos.as_view(), name='eliminarRegistroAlimentos'),
    path('auth/listarAlimentosConsumidos/', listarAlimentosConsumidos.as_view(), name='listarAlimentosConsumidos'),
    path('auth/filtrarAlimentosConsumidos/', filtrarAlimentosConsumidos.as_view(), name='filtrarAlimentosConsumidos'),
    path('api/', include(router.urls)),
]