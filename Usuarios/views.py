from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import USUARIOS, REG_USUARIOS
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

class LoginView(APIView):
    def post(self, request):
        # Obtener los datos enviados desde Ionic
        usuario = request.data.get('Usuario')
        contraseña = request.data.get('Con_Usu')

        # Validar los datos con el modelo
        try:
            usuario_obj = USUARIOS.objects.get(Usuario=usuario)
            if (contraseña ==usuario_obj.Con_Usu):
                token = RefreshToken.for_user(usuario_obj)
                tiene_registros= REG_USUARIOS.objects.filter(Usuario=usuario_obj).exists()
                return Response({'mensaje': 'Los datos son válidos', 'token': str(token.access_token), 'tieneRegistro': tiene_registros})
            else:
                return Response({'mensaje': 'Contraseña incorrecta'})
        except USUARIOS.DoesNotExist:
            return Response({'mensaje': 'Usuario no encontrado'})
        
class ObtenerDatosUsuario(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        usuario = request.user
        usuario_data = {
            'Usuario': usuario.Usuario,
            'Nom_Usu': usuario.Nom_Usu,
            'Ape_Usu': usuario.Ape_Usu,
            'Fec_Nac_usu': usuario.Fec_Nac_usu
        }
        return Response({'usuario': usuario_data})