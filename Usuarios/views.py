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
    
def guardarUsuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        nom_usu = request.POST.get('nom_usu')
        ape_usu = request.POST.get('ape_usu')
        con_usu = request.POST.get('con_usu')
        fec_nac_usu= request.POST.get('fec_nac_usu')

        usuario_obj = USUARIOS(
            Usuario = usuario,
            Nom_Usu = nom_usu,
            Ape_Usu = ape_usu,
            Con_Usu = con_usu,
            Fec_Nac_usu = fec_nac_usu
        )
        usuario_obj.save()

        return JsonResponse({'message': 'Datos guardados correctamente'})
    
    return JsonResponse({'error': 'Se requiere una solicitud POST'})