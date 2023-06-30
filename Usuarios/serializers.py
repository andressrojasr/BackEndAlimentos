from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = USUARIOS
        fields =('Usuario','Nom_Usu','Ape_Usu','Con_Usu','Fec_Nac_usu')

class RegUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = REG_USUARIOS
        fields = ('id','Fec_Reg','Est_Usu','Pes_Usu','Ind_Mas_Cor','Usuario')

class RegistroAlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = REGISTRO_ALIMENTOS
        fields = ('id','Fec_reg','Usuario')

class TipAlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TIP_ALIMENTOS
        fields = ('id','Nom_tip','Des_Tip')

class AlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALIMENTOS
        fields = ('id','Nom_Ali','Cal_Ali','Img_Ali','Cod_Tip')

class DetalleAlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DETALLE_ALIMENTOS
        fields= ('id','Cod_Reg','Id_Ali','Cantidad','Cant_calo')