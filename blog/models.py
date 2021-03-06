from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField 



class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de Publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']
    
    def __str__(self):
        return self.title

    