from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

def iniciarSesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena= request.POST.get('contrasena')
        try:
            usuario_obj= USUARIOS.objects.get(Usuario=usuario, Con_Usu=contrasena)
        except USUARIOS.DoesNotExist:
            return JsonResponse({'error': 'Credenciales inválidas'}, status=401)
        
        datos_usuario={
            'usuario': usuario_obj.Usuario,
            'nombre': usuario_obj.Nom_Usu,
            'apellido' : usuario_obj.Ape_Usu,
            'fecNac' : usuario_obj.Fec_Nac_usu,
        }
        return JsonResponse(datos_usuario)