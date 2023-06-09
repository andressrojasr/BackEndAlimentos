from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import USUARIOS

class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        usuario = request.data.get('usuario', None)
        password = request.data.get('password', None)
        user = USUARIOS (Usuario=usuario, Con_Usu=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)