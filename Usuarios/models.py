from django.db import models
from django.contrib.auth.hashers import make_password

class USUARIOS(models.Model):
    Usuario = models.CharField(max_length=20, primary_key=True)
    Nom_Usu = models.CharField(max_length=20,verbose_name='Nombre')
    Ape_Usu = models.CharField(max_length=20,verbose_name='Apellido')
    Con_Usu = models.CharField(max_length=20,verbose_name='Contraseña')
    Fec_Nac_usu = models.DateField(verbose_name='Fecha de nacimiento')

    def __str__(self):
        txt ="{0} (Nombre: {1} Apellido: {2})"
        return txt.format(self.Usuario, self.Nom_Usu, self.Ape_Usu)
    
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
    
class REG_USUARIOS(models.Model):
    Fec_Reg = models.DateField(auto_now_add=True, auto_now=False,verbose_name='Fecha de registro')
    Est_Usu = models.FloatField(verbose_name='Estatura')
    Pes_Usu = models.FloatField(verbose_name='Peso')
    Ind_Mas_Cor= models.FloatField(null=True,verbose_name='IMC')
    Usuario = models.ForeignKey(USUARIOS, on_delete=models.CASCADE)

    def __str__(self):
        txt ="{0} (Fecha: {1})"
        return txt.format(self.Usuario, self.Fec_Reg)
    
    class Meta:
        verbose_name="Registros de IMC de Usuario"
        verbose_name_plural="Registros de IMC Usuarios"

class REGISTRO_ALIMENTOS(models.Model):
    Fec_reg = models.DateField(verbose_name='Fecha de registro')
    Usuario = models.ForeignKey(USUARIOS, on_delete=models.CASCADE)

    def __str__(self):
        txt ="{0} (Fecha: {1})"
        return txt.format(self.Usuario, self.Fec_reg)
    
    class Meta:
        verbose_name="Registro de Alimentos Consumidos"
        verbose_name_plural="Registros de Alimentos Consumidos"

class TIP_ALIMENTOS(models.Model):
    Nom_tip = models.CharField(max_length=20,verbose_name='Nombre')
    Des_Tip = models.CharField(max_length=50, null=True,verbose_name='Descripción')

    def __str__(self):
        txt ="{0}"
        return txt.format(self.Nom_tip)
    
    class Meta:
        verbose_name="Tipo de Alimento"
        verbose_name_plural="Tipos de Alimentos"

class ALIMENTOS(models.Model):
    Nom_Ali = models.CharField(max_length=20,verbose_name='Nombre')
    Cal_Ali = models.IntegerField(verbose_name='Calorias')
    Cod_Tip = models.ForeignKey(TIP_ALIMENTOS, on_delete=models.CASCADE,verbose_name='Tipo de alimento')

    def __str__(self):
        txt ="{0} (Calorias: {1})"
        return txt.format(self.Nom_Ali, self.Cal_Ali)
    
    class Meta:
        verbose_name="Alimento"
        verbose_name_plural="Alimentos"

class DETALLE_ALIMENTOS(models.Model):
    Cod_Reg = models.ForeignKey(REGISTRO_ALIMENTOS, on_delete=models.CASCADE,verbose_name='Código')
    Id_Ali = models.ForeignKey(ALIMENTOS, on_delete=models.CASCADE,verbose_name='Alimento')
    Cantidad= models.FloatField(null=True)
    Cant_calo = models.FloatField(null=True,verbose_name='Total calorias')

    def __str__(self):
        txt ="{0} (Id Alimento: {1} Cantidad calorias: {2})"
        return txt.format(self.Cod_Reg, self.Id_Ali, self.Cant_calo)
    
    class Meta:
        verbose_name="Detalle de Alimentos Consumidos"
        verbose_name_plural="Detalles de Alimentos Consumidos"
    
