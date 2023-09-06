from django.db import models
from django.template.defaultfilters import slugify
import datetime
#from Usuarios.models import Autor
from django.contrib.auth.models import User

# Create your models here.

'''class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    suscripcion = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.suscripcion} - {self.email}'
'''

'''class Nota(models.Model):
    titulo = models.CharField(max_length=50)
    bajada = models.CharField(max_length=80)
    texto = models.TextField
    fecha = models.DateField()
    img_destacada = models.ImageField()
    estatus = models.BooleanField()
    autor = models.ForeignKey(Autor, on_delete=models.SET_DEFAULT, default=None)
    def __str__(self):
        return f'{self.titulo} \n{self.bajada} \n{self.img_destacada} \n{self.fecha} - {self.autor} \n{self.texto}'
'''    


class Blog(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()    
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    usuario_autor = models.OneToOneField(User, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    web = models.URLField(max_length=200, blank=True)
    suscripcion = models.IntegerField()
    foto = models.ImageField(
        upload_to='Usuarios/imagenes',
        blank=True,
        null=True
    )
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.usuario_autor.username} - {self.foto}'
    
class Lector(models.Model):
    usuario_lector = models.OneToOneField(User, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    foto = models.ImageField(
        upload_to='Usuarios/imagenes',
        blank=True,
        null=True
    )
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.usuario_lector.username} - {self.foto}'
    
class Nota(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.PROTECT)
    titulo = models.CharField(max_length=100)
    bajada = models.CharField(max_length=120)
    texto = models.TextField()
    fecha_publicacion = models.DateField()
    autores = models.ManyToManyField(Autor)
    img_destacada = models.ImageField()
    estatus = models.BooleanField()
    url = models.URLField(slugify)
    def __str__(self):
        return f'{self.titulo} - {self.bajada} - {self.estatus}'
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return super().__str__()