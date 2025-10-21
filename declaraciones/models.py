from django.db import models

class DeclaracionJurada(models.Model):
    tipo_declaración = models.CharField(max_length=100)
    fecha_extraccion = models.DateTimeField()
    estado_declaracion = models.CharField(max_length=60)

    def __str__(self):
        return self.tipo_declaración


