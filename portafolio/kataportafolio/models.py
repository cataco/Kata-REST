from django.db import models


class Portafolios(models.Model):
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    publico = models.BooleanField()

    def __str__(self):
        return self.nombre
