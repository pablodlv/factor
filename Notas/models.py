from django.db import models
from django.template.defaultfilters import slugify
import datetime
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
    web = models.URLField(max_length=200, blank=True)
    suscripcion = models.IntegerField()
    foto = models.ImageField(
        upload_to='Usuarios/imagenes',
        blank=True,
        null=True
    )
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.usuario_autor.username} - {self.suscripcion}'


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'
    
class Nota(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.PROTECT)
    titulo = models.CharField(max_length=100)
    bajada = models.CharField(max_length=120)
    texto = models.TextField()
    fecha_publicacion = models.DateField()
    autor = models.ManyToManyField(Autor)
    categoria_nota = models.ManyToManyField(Categoria)
    etiqueta_nota = models.ManyToManyField(Etiqueta)
    img_destacada = models.ImageField(
        upload_to='imagenes/destacadas',
        blank=True,
        null=True
    )
    estatus_publicacion = models.BooleanField()
    #url = models.URLField(slugify)
    def __str__(self):
        return f'{self.titulo} - {self.categoria_nota} - {self.estatus_publicacion}'
    