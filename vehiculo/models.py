
from django.db import models

class Vehiculo(models.Model):
    # Definir los diferentes tipos de vehículos
    TIPO_CHOICES = [
        ('camion', 'Camión'),
        ('camioneta', 'Camioneta'),
        ('motoneta', 'Motoneta'),
        ('furgon', 'Furgón'),
    ]
    
    tipo = models.CharField(
        max_length=50, 
        choices=TIPO_CHOICES, 
        null=False, 
        blank=False
    )
    
    placa = models.CharField(
        max_length=10, 
        unique=True,  # La placa debe ser única
        null=False, 
        blank=False
    )
    
    ubicacion_actual = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
    )
    
    estado = models.CharField(
        max_length=50, 
        null=False, 
        blank=False,
        default='activo'
    )
    
    kilometraje = models.PositiveIntegerField(
        null=False, 
        blank=False,
        default=0
    )
    
    sensor = models.CharField(
        max_length=100, 
        null=False, 
        blank=False,
        default='activo'
    )
    
    conductor = models.CharField(
        max_length=100, 
        null=False, 
        blank=False
    )
    
    mantenimiento_ruta_actual = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
    )
    
    ruta = models.CharField(
       max_length=255, 
        null=True, 
        blank=True
    )
    
    reporte = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return f"{self.tipo} - {self.placa}"
