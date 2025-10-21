from django.db import models
from datetime import datetime
from instrumentos.models import Instrumento 
from usuarios.models import Usuario
from declaraciones.models import DeclaracionJurada


class CalificacionTributaria(models.Model):
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    declaracion = models.ForeignKey(DeclaracionJurada, on_delete=models.CASCADE)
    factor = models.ForeignKey('auditoria.FactorMensual', on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField()
    descripcion = models.CharField(max_length=200)
    secuencia_evento = models.IntegerField()
    dividendo = models.FloatField()
    valor_historico = models.FloatField()
    año_tributario = models.DateField()
    isfut = models.BooleanField(default=False)
    origen = models.CharField(max_length=80)
    estado_tributario = models.CharField(max_length=50)

    def __str__(self):
        return self.instrumento.nombre





class FactorMensual(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor_factor = models.FloatField()
    fecha_factor = models.DateField()
    regimen = models.CharField(max_length=200)

    def __str__(self):
        return self.fecha_factor


class Reportes(models.Model):
    Estado_Choices = [
        ('pendiente' , 'Pendiente'),
        ('revisado', 'Revisado'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(help_text="Detalles del error encontrado")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reportes_creados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices= Estado_Choices, default='pendiente')

    def __str__(self):
        return self.titulo
