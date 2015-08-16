from django.db import models


class Cliente(models.Model):
        nombre    = models.CharField(max_length=200)
        apellidos = models.CharField(max_length=200)
        primerServicio = models.DateField('fecha primer Servicio')


class Venta(models.Model):
        CONTADO = 'CONTADO'
        CREDITO = 'CREDITO'
        OPCIONES_VENTA = ((CONTADO,'Contado'),(CREDITO,'Credito'))
        cliente = models.ForeignKey(Cliente)
        Fecha = models.DateField('fecha venta')
        contado = models.CharField(max_length=20,
                                      choices=OPCIONES_VENTA,
                                      default=CONTADO)
        precio = models.DecimalField(max_digits=5, decimal_places=2)
        cantidad = models.PositiveSmallIntegerField()


class Cobro(models.Model):
        Cliente = models.ForeignKey(Cliente)
