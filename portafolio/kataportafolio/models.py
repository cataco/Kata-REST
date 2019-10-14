from django.contrib.auth.models import User
from django.db import models


class Portafolio(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    publico = models.BooleanField()
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    link_imagen = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    tipo_archivo= models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
