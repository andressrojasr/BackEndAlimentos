from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

def iniciarSesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        con_usu = request.POST.get('contrasena')
        return JsonResponse(usuario)    

   #    try:
   #         usuario_obj = USUARIOS.objects.get(Usuario=usuario)
            
    #        if usuario_obj.Con_Usu == con_usu:
                # Usuario y Con_Usu son correctos
     #           return JsonResponse(True)
      #      else:
                # Contraseña incorrecta
      #          return JsonResponse(False)
       # except USUARIOS.DoesNotExist:
            # Usuario no encontrado
        #    return JsonResponse({'mensaje': 'Usuario no encontrado'})#

    else:
        # Método de solicitud no válido
        return JsonResponse({'mensaje': 'Método no válido'})
    
def guardarUsuario(request):
    if request.method == 'Post':
        usuario = request.Post.get('usuario')
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