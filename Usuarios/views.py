from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TIP_ALIMENTOS

class LoginView(APIView):
    def post(self, request):
        # Obtener los datos enviados desde Ionic
        usuario = request.data.get('Nom_Tip')
        contrasena = request.data.get('Des_Tip')
        # Validar los datos con el modelo
        try:
            usuario_obj = TIP_ALIMENTOS.objects.get(Nom_Tip=usuario)
            if check_password(contrasena, usuario_obj.Des_Tip):
                return Response({'mensaje': 'Los datos son válidos'})
            else:
                return Response({'mensaje': 'Contraseña incorrecta'})
        except TIP_ALIMENTOS.DoesNotExist:
            return Response({'mensaje': 'Usuario no encontrado'})