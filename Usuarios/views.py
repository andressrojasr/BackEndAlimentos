from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import USUARIOS
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken



#class LoginView(APIView):
 #   def post(self, request):
        # Obtener los datos enviados desde Ionic
  #      usuario = request.data.get('Usuario')
   #     contraseña = request.data.get('Con_Usu')

        # Validar los datos con el modelo
    #    try:
     #       usuario_obj = USUARIOS.objects.get(Usuario=usuario)
      #      if (contraseña ==usuario_obj.Con_Usu):
      #          return Response({'mensaje': 'Los datos son válidos'})
       #     else:
        #        return Response({'mensaje': 'Contraseña incorrecta'})
       # except USUARIOS.DoesNotExist:
        #    return Response({'mensaje': 'Usuario no encontrado'})

class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('Usuario')
        password = request.data.get('Con_Usu')

        try:
            user = USUARIOS.objects.get(Usuario=username)
            if (user.Con_Usu == password):
                print(user.Usuario)
                print(user.Nom_Usu)
                print(user.Ape_Usu)
                print(user.Con_Usu)
                print(user.Fec_Nac_usu)
                refresc= RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresc),
                    'access': str(refresc.access_token),
                    'mensaje': 'Los datos son válidos',
                })
            else:
                return Response({'mensaje': 'Contraseña incorrecta'})
        except USUARIOS.DoesNotExist:
            return Response({'mensaje': 'Usuario no encontrado'})