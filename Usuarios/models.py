from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''class Lector(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    web = models.URLField(max_length=200, blank=True)
    email = models.EmailField()
    foto = models.ImageField(
        upload_to='Usuarios/imagenes',
        blank=True,
        null=True
    )
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.usuario.username
    
class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    suscripcion = models.IntegerField()
    email = models.EmailField()
    foto = models.ImageField(
        upload_to='Usuarios/imagenes',
        blank=True,
        null=True
    )
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.usuario.username} \n {self.nombre} - {self.apellido} \n {self.suscripcion} - {self.email}'
    
'''
'''class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email}'
'''

