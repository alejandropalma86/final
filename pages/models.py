from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField 

class Page(models.Model):
    title = models.CharField(verbose_name='Título', max_length=200)
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['title']
    
    def __str__(self):
        return self.title

