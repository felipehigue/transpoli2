from django.db import models

# Create your models here.



class Usuario(models.Model):
    
    CONDUCTOR = 'conductor'
    MONITOR = 'monitor'
    ADMIN = 'admin'
    
    ROLES = [
        (CONDUCTOR, 'Conductor'),
        (MONITOR, 'Monitor'),
        (ADMIN, 'Admin'),
    ]
    
    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default=CONDUCTOR,
        null=False,
        blank=False,
    )
    nombre = models.CharField(max_length=100, null=False, blank=False) 
    

    def __str__(self):
        return self.nombre


class Credenciales(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)  
    email = models.EmailField(unique=True, null=False, blank=False)
    contraseña = models.CharField(max_length=100, null=False , blank=False)

    def __str__(self):
        return self.email
