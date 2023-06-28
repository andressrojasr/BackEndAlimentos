from .models import  *
from rest_framework import viewsets, permissions
from .serializers import *

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = USUARIOS.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuariosSerializer

class RegUsuariosViewSet(viewsets.ModelViewSet):
    queryset = REG_USUARIOS.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegUsuariosSerializer

class RegistroAlimentosViewSet(viewsets.ModelViewSet):
    queryset = REGISTRO_ALIMENTOS.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistroAlimentosSerializer

class TipAlimentosViewSet(viewsets.ModelViewSet):
    queryset = TIP_ALIMENTOS.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipAlimentosSerializer

class AlimentosViewSet(viewsets.ModelViewSet):
    queryset = ALIMENTOS.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlimentosSerializer

class DetalleAlimentosViewSet(viewsets.ModelViewSet):
    queryset = DETALLE_ALIMENTOS.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DetalleAlimentosSerializer
