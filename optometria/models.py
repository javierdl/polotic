from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.template.defaultfilters import default

# Create your models here.
class Role(models.Model):
#     roles = models.ManyToManyField(Role)
    SECRETARIA = 1
    MEDICO     = 2
    VENTAS     = 3
    TALLER     = 4
    GERENCIA   = 5

    ROLE_CHOICES = (
        (SECRETARIA, 'Secretaría'),
        (MEDICO,     'Profesional médico'),
        (VENTAS,     'Ventas'),
        (TALLER,     'Taller'),
        (GERENCIA,   'Gerencia'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)


class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_corto = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
    

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.IntegerField()


class Turno(models.Model):
    fecha_hora = models.DateTimeField(default=timezone.now)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)


class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    observacion = models.TextField(default='')
    fecha_hora = models.DateTimeField(default=timezone.now)


class Producto(models.Model):
    precio = models.FloatField()


class Pedido(models.Model):
    LENTE_LEJOS     = 1
    LENTE_CERCA     = 2
    LENTE_IZQUIERDA = 3
    LENTE_DERECHA   = 4
    
    LENTES_CHOICES = (
        (LENTE_LEJOS,     'Lejos'),
        (LENTE_CERCA,     'Cerca'),
        (LENTE_IZQUIERDA, 'Izquierda'),
        (LENTE_DERECHA,   'Derecha'),
    )
    
    PEDIDO_PENDIENTE  = 1
    PEDIDO_PEDIDO     = 2
    PEDIDO_TALLER     = 3
    PEDIDO_FINALIZADO = 4
    
    PEDIDO_CHOICES = (
        (PEDIDO_PENDIENTE,  'Pendiente'),
        (PEDIDO_PEDIDO,     'Pedido'),
        (PEDIDO_PEDIDO,     'Taller'),
        (PEDIDO_FINALIZADO, 'Finalizado'),
    )
    
    CREDITO   = 1
    DEBITO    = 2
    BILLETERA = 3
    EFECTIVO  = 4
    
    TIPO_PAGO_CHOICES = (
        (CREDITO,   'Tarjeta de crédito'),
        (DEBITO,    'Tarjeta de Débito'),
        (BILLETERA, 'Billetera virtual'),
        (EFECTIVO,  'Efectivo'),
    )

    tipo_pago = models.PositiveSmallIntegerField(choices=TIPO_PAGO_CHOICES, default=DEBITO)
    producto = models.ManyToManyField(Producto)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=50)
    lente = models.PositiveSmallIntegerField(choices=LENTES_CHOICES, default=None)
    armazon = models.BooleanField(default=False)
    pedido = models.PositiveSmallIntegerField(choices=PEDIDO_CHOICES, default=PEDIDO_PENDIENTE)






