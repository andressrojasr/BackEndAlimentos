from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import USUARIOS
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView



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
            if user.Con_Usu == password:
                refresh = RefreshToken.for_user(user)
                return Response({
                    #'access': str(RefreshToken.access_token),
                    #'refresh': str(refresh),
                    'mensaje': 'Los datos son válidos',
                })
            else:
                return Response({'mensaje': 'Contraseña incorrecta'})
        except USUARIOS.DoesNotExist:
            return Response({'mensaje': 'Usuario no encontrado'})