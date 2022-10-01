from django.db import models
from HospitalHomeBE.models.usuario import Usuario

class Familiar(models.Model):
    id = models.BigAutoField(primary_key = True)
    parentezco = models.CharField(max_length=40, null=True)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)