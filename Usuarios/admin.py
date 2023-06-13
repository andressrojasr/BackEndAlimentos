from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import USUARIOS, TIP_ALIMENTOS, REGISTRO_ALIMENTOS, ALIMENTOS, DETALLE_ALIMENTOS, REG_USUARIOS
from django.utils.translation import ugettext_lazy


class MyAdminSite(AdminSite):
    site_header = ugettext_lazy('My administration')
AdminSite=MyAdminSite()


@admin.register(USUARIOS)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('Usuario','Nom_Usu','Ape_Usu','Fec_Nac_usu')
    ordering=('Usuario',)
    search_fields=('Usuario','Nom_Usu','Ape_Usu')
    list_display_links=('Usuario',)
    #list_editable('Usuario',)

@admin.register(REG_USUARIOS)
class RegUsuariosAdmin(admin.ModelAdmin):
    list_display=('Usuario','Est_Usu','Pes_Usu','Ind_Mas_Cor','Fec_Reg')
    ordering=('Usuario',)
    search_fields=('Usuario','Fec_Reg')

@admin.register(REGISTRO_ALIMENTOS)
class RegistroAlimentosAdmin(admin.ModelAdmin):
    list_display=('Usuario','Fec_reg')
    ordering=('Usuario',)
    search_fields=('Usuario','Fec_reg')


@admin.register(TIP_ALIMENTOS)
class TipAlimentosAdmin(admin.ModelAdmin):
    list_display=('Nom_tip','Des_Tip')
    ordering=('Nom_tip',)
    search_fields=('Nom_tip','Des_Tip')

@admin.register(ALIMENTOS)
class AlimentosAadmin(admin.ModelAdmin):
    list_display=('Img_Ali','Nom_Ali','Cal_Ali','Cod_Tip')
    ordering=('Nom_Ali',)
    search_fields=('Nom_Ali','Cod_Tip','Cod_Tip')

@admin.register(DETALLE_ALIMENTOS)
class DetalleAlimentosAdmin(admin.ModelAdmin):
    list_display=('Cod_Reg','Id_Ali','Cant_calo')
    ordering=('Cod_Reg',)
    search_fields=('Cod_Reg','Id_Ali')



