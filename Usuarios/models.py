from django.db import models

class USUARIOS(models.Model):
    Usuario = models.CharField(max_length=20, primary_key=True)
    Nom_Usu = models.CharField(max_length=20)
    Ape_Usu = models.CharField(max_length=20)
    Con_Usu = models.CharField(max_length=25)
    Fec_Nac_usu = models.DateField()

class REG_USUARIOS(models.Model):
    Fec_Reg = models.DateField()
    Est_Usu = models.FloatField()
    Pes_Usu = models.FloatField()
    Ind_Mas_Cor= models.FloatField(null=True)
    Usuario = models.ForeignKey(USUARIOS, on_delete=models.CASCADE)

class REGISTRO_ALIMENTOS(models.Model):
    Fec_reg = models.DateField()
    Usuario = models.ForeignKey(USUARIOS, on_delete=models.CASCADE)

class TIP_ALIMENTOS(models.Model):
    Nom_tip = models.CharField(max_length=20)
    Des_Tip = models.CharField(max_length=50, null=True)

class ALIMENTOS(models.Model):
    Nom_Ali = models.CharField(max_length=20)
    Cal_Ali = models.IntegerField()
    Img_Ali = models.ImageField()
    Cod_Tip = models.ForeignKey(TIP_ALIMENTOS, on_delete=models.CASCADE)

class DETALLE_ALIMENTOS(models.Model):
    Cod_Reg = models.ForeignKey(REGISTRO_ALIMENTOS, on_delete=models.CASCADE)
    Id_Ali = models.ForeignKey(ALIMENTOS, on_delete=models.CASCADE)
    Cant_calo = models.FloatField(null=True)

class ADMINISTRADORES(models.Model):
    Usu_Adm = models.CharField(max_length=20, primary_key=True)
    Con_Adm = models.CharField(max_length=25)
    Cor_Adm = models.EmailField()