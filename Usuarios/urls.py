from rest_framework import routers
from .api import *
from .views import LoginView, ExisteRegistro, InsertarRegistro, listarRegistros, editarRegistro, eliminarRegistro
from django.urls import path, include

router = routers.DefaultRouter()

router.register('Usuarios',UsuariosViewSet, 'usuarios')
router.register('RegUsuarios',RegUsuariosViewSet, 'RegUsuarios')
router.register('RegAlimentos',RegistroAlimentosViewSet, 'RegAlimentos')
router.register('TipAlimentos',TipAlimentosViewSet, 'TipAlimentos')
router.register('Alimentos',AlimentosViewSet, 'Alimentos')
router.register('DetAlimentos',DetalleAlimentosViewSet, 'DetAlimentos')
router.register('Administradores', AdministradoresViewSet,'Administradores')

urlpatterns = [
    path('auth/loginView/', LoginView.as_view(), name='loginView'),
    path('auth/existeRegistro/', ExisteRegistro.as_view(), name='existeRegistro'),
    path('auth/insertarRegistro/', InsertarRegistro.as_view(), name='insertarRegistro'),
    path('auth/listarRegistros/', listarRegistros.as_view(), name='listarRegistros'),
    path('auth/editarRegistro/', editarRegistro.as_view(), name='editarRegistro'),
    path('auth/eliminarRegistro/', eliminarRegistro.as_view(), name='eliminarRegistro'),
    path('api/', include(router.urls)),
]