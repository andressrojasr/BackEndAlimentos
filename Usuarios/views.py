from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import USUARIOS, REG_USUARIOS



class LoginView(APIView):
    def post(self, request):
        # Obtener los datos enviados desde Ionic
        usuario = request.data.get('Usuario')
        contraseña = request.data.get('Con_Usu')

        # Validar los datos con el modelo
        try:
            usuario_obj = USUARIOS.objects.get(Usuario=usuario)
            if (contraseña ==usuario_obj.Con_Usu):
                return Response({'mensaje': 'Los datos son válidos'})
            else:
                return Response({'mensaje': 'Contraseña incorrecta'})
        except USUARIOS.DoesNotExist:
            return Response({'mensaje': 'Usuario no encontrado'})


class ExisteRegistro(APIView):
    def post(self, request):
        usuario = request.data.get('Usuario')
        try:
            registro = REG_USUARIOS.objects.get(Usuario=usuario)
            return Response({'mensaje': 'Si'})
        except REG_USUARIOS.DoesNotExist:
            return Response({'mensaje': 'No'})