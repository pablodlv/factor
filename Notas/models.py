from django.db import models
from django.template.defaultfilters import slugify
import datetime
from Usuarios.models import Autor

# Create your models here.

'''class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    suscripcion = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.suscripcion} - {self.email}'
'''

class Nota(models.Model):
    titulo = models.CharField(max_length=50)
    bajada = models.CharField(max_length=80)
    texto = models.TextField
    fecha = models.DateField()
    img_destacada = models.ImageField()
    categoria = models.TextChoices
    estatus = models.BooleanField()
    autor = models.ForeignKey(Autor, on_delete=models.SET_DEFAULT, default=None)
    def __str__(self):
        return f'{self.titulo} \n{self.bajada} \n{self.img_destacada} \n{self.fecha} - {self.autor} \n{self.texto}'




