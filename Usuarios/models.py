from django.db import models
from django.contrib.auth.hashers import make_password

class USUARIOS(models.Model):
    Usuario = models.CharField(max_length=20, primary_key=True)
    Nom_Usu = models.CharField(max_length=20)
    Ape_Usu = models.CharField(max_length=20)
    Con_Usu = models.CharField(max_length=20)
    Fec_Nac_usu = models.DateField()

    def __str__(self):
        txt ="{0} (Nombre: {1} Apellido: {2})"
        return txt.format(self.Usuario, self.Nom_Usu, self.Ape_Usu)
    
class REG_USUARIOS(models.Model):
    Fec_Reg = models.DateField()
    Est_Usu = models.FloatField()
    Pes_Usu = models.FloatField()
    Ind_Mas_Cor= models.FloatField(null=True)
    Usuario = models.ForeignKey(USUARIOS, on_delete=models.CASCADE)

    def __str__(self):
        txt ="{0} (Fecha: {1})"
        return txt.format(self.Usuario, self.Fec_Reg)

class REGISTRO_ALIMENTOS(models.Model):
    Fec_reg = models.DateField()
    Usuario = models.ForeignKey(USUARIOS, on_delete=models.CASCADE)

    def __str__(self):
        txt ="{0} (Fecha: {1})"
        return txt.format(self.Usuario, self.Fec_reg)

class TIP_ALIMENTOS(models.Model):
    Nom_tip = models.CharField(max_length=20)
    Des_Tip = models.CharField(max_length=50, null=True)

    def __str__(self):
        txt ="{0}"
        return txt.format(self.Nom_tip)

class ALIMENTOS(models.Model):
    Nom_Ali = models.CharField(max_length=20)
    Cal_Ali = models.IntegerField()
    Img_Ali = models.ImageField()
    Cod_Tip = models.ForeignKey(TIP_ALIMENTOS, on_delete=models.CASCADE)

    def __str__(self):
        txt ="{0} (Calorias: {1})"
        return txt.format(self.Nom_Ali, self.Cal_Ali)

class DETALLE_ALIMENTOS(models.Model):
    Cod_Reg = models.ForeignKey(REGISTRO_ALIMENTOS, on_delete=models.CASCADE)
    Id_Ali = models.ForeignKey(ALIMENTOS, on_delete=models.CASCADE)
    Cant_calo = models.FloatField(null=True)

    def __str__(self):
        txt ="{0} (Id Alimento: {1} Cantidad calorias: {2})"
        return txt.format(self.Cod_Reg, self.Id_Ali, self.Cant_calo)

class ADMINISTRADORES(models.Model):
    Usu_Adm = models.CharField(max_length=20, primary_key=True)
    Con_Adm = models.CharField(max_length=25)
    Cor_Adm = models.EmailField()
    
    def __str__(self):
        txt ="{0} (Usuario: {1} Correo: {2})"
        return txt.format(self.Usu_Adm, self.Cor_Adm)