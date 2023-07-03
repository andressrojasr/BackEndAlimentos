from rest_framework.views import APIView
from rest_framework.response import Response
from .models import USUARIOS, REG_USUARIOS, REGISTRO_ALIMENTOS, DETALLE_ALIMENTOS, ALIMENTOS, TIP_ALIMENTOS
from datetime import date
from .serializers import *



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
            registro = REG_USUARIOS.objects.filter(Usuario=usuario)
            if registro.exists():
                return Response({'mensaje': 'Si'})
            else:
                return Response({'mensaje': 'No'})
        except REG_USUARIOS.DoesNotExist:
            return Response({'mensaje': 'No'})
        
class InsertarRegistro(APIView):
    def post(self, request):
        try:
            estatura = float(request.data.get('Estatura'))
            peso = float(request.data.get('Peso'))
            usuario = request.data.get('Usuario')
            imc = round(peso/((estatura/100)*(estatura/100)),2)

            existe=REG_USUARIOS.objects.filter(Usuario= usuario, Fec_Reg=date.today()).exists()
            if existe:
                return Response({'mensaje': 'Ya existe un registro en la fecha indicada'})
            
            registro = REG_USUARIOS(
                Est_Usu= estatura,
                Pes_Usu= peso,
                Ind_Mas_Cor=imc,
                Usuario = USUARIOS.objects.get(Usuario=usuario)

            )

            registro.save()

            return Response({
                'fecha': registro.Fec_Reg,
                'estatura': registro.Est_Usu,
                'peso': registro.Pes_Usu,
                'imc': registro.Ind_Mas_Cor,
                'usuario': registro.Usuario.Usuario,
                'mensaje': 'true'
            })
        except Exception as e:
            return Response({'mensaje': str(e)})
        
class listarRegistros(APIView):
    def post(self, request):
        try:
            usuario = request.data.get('Usuario')

            reg_usuarios = REG_USUARIOS.objects.filter(Usuario=usuario).order_by('-Fec_Reg')

            serializer = RegUsuariosSerializer(reg_usuarios, many=True)

            return Response(serializer.data)
        except Exception as e:
            return Response({'mensaje': str(e)})

class editarRegistro(APIView):
    def put(self, request):
        try: 
            fecha= request.data.get('Fec_Reg')
            usuario= request.data.get('Usuario')
            estatura = float(request.data.get('Est_Usu'))
            peso = float(request.data.get('Pes_Usu'))
            imc = round(peso/((estatura/100)*(estatura/100)),2)
            registro = REG_USUARIOS.objects.get(Fec_Reg=fecha, Usuario=usuario)
            registro.Est_Usu = estatura
            registro.Pes_Usu=peso
            registro.Ind_Mas_Cor= imc
            registro.save()
            return Response({'mensaje': 'true'})
        except REG_USUARIOS.DoesNotExist:
            return Response({'mensaje': 'Error al actualizar'})
        
        
    
class eliminarRegistro(APIView):
    def post(self, request):
        try:
            fecha = request.data.get('Fec_Reg')
            usuario = request.data.get('Usuario')
            registro = REG_USUARIOS.objects.get(Fec_Reg= fecha, Usuario= usuario)
            registro.delete()

            return Response({'mensaje': 'true'})
        except REG_USUARIOS.DoesNotExist:
            return Response({'mensaje': 'Registro no encontrado'})
        
class filtrarRegistro(APIView):
    def post(self, request):
        try:
            fechaInicio = request.data.get('Fec_Ini')
            fechaFin = request.data.get('Fec_Fin')
            usuario = request.data.get('Usuario')
            
            registros = REG_USUARIOS.objects.filter(Fec_Reg__gte=fechaInicio, Fec_Reg__lte=fechaFin, Usuario=usuario).order_by('-Fec_Reg')
            serializer = RegUsuariosSerializer(registros, many=True)
            return Response(serializer.data)
        except REG_USUARIOS.DoesNotExist:
            return Response({'mensaje': 'Registro no encontrado'})
            
class insertarRegistroAlimentos(APIView):
    def post(self, request):
        try:
            fecha = request.data.get('Fec_Reg')
            usuario = request.data.get('Usuario')
            alimentos = request.data.get('alimentos')
            registro = REGISTRO_ALIMENTOS.objects.filter(Usuario=usuario, Fec_reg=fecha)
            if registro.exists():
                return Response({'mensaje': 'Ya existe un registro en la fecha indicada'})
            else:
                registroNuevo = REGISTRO_ALIMENTOS(
                    Fec_reg= fecha,
                    Usuario= USUARIOS.objects.get(Usuario=usuario)
                )

                registroNuevo.save()

                for alimento in alimentos:
                    idAli= alimento.get('id_Ali')
                    cantidad = float(alimento.get('Cantidad'))
                    
                    alimento_obj= ALIMENTOS.objects.get(id=idAli)
                    cantCalo=round((float(alimento_obj.Cal_Ali)*cantidad),2)

                    detalle= DETALLE_ALIMENTOS(
                        Cod_Reg= registroNuevo,
                        Id_Ali= ALIMENTOS.objects.get(id=idAli),
                        Cantidad=cantidad,
                        Cant_calo=cantCalo
                    )
                    detalle.save()
                return Response({'mensaje': 'true'})
        except REGISTRO_ALIMENTOS.DoesNotExist:
            return Response({'mensaje': 'false'})

class listarRegistrosAlimentos(APIView):
    def post(self, request):
        try:
            usuario = request.data.get('Usuario')
            reg_usuarios = REGISTRO_ALIMENTOS.objects.filter(Usuario=usuario).order_by('-Fec_reg')
            serializer = RegistroAlimentosSerializer(reg_usuarios, many=True)
            detalle_reg = DETALLE_ALIMENTOS.objects.filter(Cod_Reg__Usuario=usuario)
            detalleSerializer=DetalleAlimentosSerializer(detalle_reg,many=True)
            return Response({'registros':serializer.data,'detalles':detalleSerializer.data})
        except Exception as e:
            return Response({'mensaje': str(e)})
        
class filtrarRegistrosAlimentos(APIView):
    def post(self, request):
        try:
            usuario = request.data.get('Usuario')
            fechaIni = request.data.get('Fec_Ini')
            fechaFin = request.data.get('Fec_Fin')
            reg_usuarios = REGISTRO_ALIMENTOS.objects.filter(Usuario=usuario, Fec_reg__gte=fechaIni, Fec_reg__lte=fechaFin).order_by('-Fec_reg')
            serializer = RegistroAlimentosSerializer(reg_usuarios, many=True)
            detalle_reg = DETALLE_ALIMENTOS.objects.filter(Cod_Reg__Usuario=usuario,Cod_Reg__Fec_reg__gte=fechaIni, Cod_Reg__Fec_reg__lte=fechaFin)
            detalleSerializer=DetalleAlimentosSerializer(detalle_reg,many=True)
            return Response({'registros':serializer.data,'detalles':detalleSerializer.data})
        except Exception as e:
            return Response({'mensaje': str(e)})
        
class listarTiposDeAlimentos(APIView):
    def get(self, request):
        try:
            tiposAlimentos= TIP_ALIMENTOS.objects.all()
            serializer= TipAlimentosSerializer(tiposAlimentos, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'mensaje': str(e)})
        
class listarAlimentos(APIView):
    def post(self, request):
        try:
            idTip=request.data.get('Id_Tip')
            alimentos=ALIMENTOS.objects.filter(Cod_Tip=idTip).order_by('Nom_Ali')
            serializer= AlimentosSerializer(alimentos, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'mensaje': str(e)})
        
class editarRegistroAlimentos(APIView):
    def post(self, request):
        try:
            detalles= request.data.get('alimentos')
            registro= request.data.get('id')

            registro= REGISTRO_ALIMENTOS.objects.get(id=registro)

            DETALLE_ALIMENTOS.objects.filter(Cod_Reg=registro).exclude(id__in=[detalle.get('id') for detalle in detalles]).delete()

            for detalle in detalles:
                detalleId= detalle.get('id')
                idAli= detalle.get('id_Ali')
                cantidad= float(detalle.get('cantidad'))
                cantCalo = float(detalle.get('Can_Calo'))

                if detalleId:
                    try:
                        alimento= ALIMENTOS.objects.get(id=idAli)
                        detalleAlimentos=DETALLE_ALIMENTOS.objects.get(id=detalleId)
                        detalleAlimentos.Cantidad=cantidad
                        detalleAlimentos.Id_Ali= alimento
                        detalleAlimentos.Cant_calo=(cantidad*cantCalo)
                        detalleAlimentos.save()
                    except Exception as e:
                        return Response({'mensaje': str(e)})
                else:
                    DETALLE_ALIMENTOS.objects.create(Cod_Reg=registro,Cantidad=cantidad,Cant_calo=(cantidad*cantCalo))
            
            return Response({'mensaje':'Registro actualizado exitosamente'})
        except Exception as e:
            return Response({'mensaje': str(e)})