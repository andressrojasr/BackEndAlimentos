from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import USUARIOS, REG_USUARIOS
from datetime import date



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
        
class InsertarRegistro(APIView):
    def post(self, request):
        try:
            estatura = request.data.get('Estatura')
            peso = request.data.get('Peso')
            usuario = request.data.get('Usuario')
            imc = peso/(estatura**2)

            existe=REG_USUARIOS.objects.filter(Usuario= usuario, Fec_Reg=date.today()).exists()
            if existe:
                return Response({'mensaje': 'Ya existe un registro en la fecha indicada'})
            
            registro = REG_USUARIOS(
                Est_Usu= estatura,
                Pes_Usu= peso,
                Ind_Mas_Cor=imc,
                Usuario =usuario

            )

            registro.save()

            return Response({
                'fecha': registro.Fec_Reg,
                'estatura': registro.Est_Usu,
                'peso': registro.Pes_Usu,
                'imc': registro.Ind_Mas_Cor,
                'usuario': registro.Usuario
            })
        except Exception as e:
            return Response({'mensaje': str(e)})



        