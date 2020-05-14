from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 


class JobVacancy(models.Model):
    position = models.CharField(max_length=100, verbose_name='Puesto')
    education = models.CharField(max_length=100, verbose_name='Escolaridad')
    experience = models.CharField(max_length=100, verbose_name='Experiencia')
    age = models.CharField(max_length=100, verbose_name='Edad')
    languages  = models.CharField(max_length=100, verbose_name='Idiomas')
    knowledge = RichTextField(verbose_name='Conocimientos')
    activities  = RichTextField(verbose_name='Actividades')
    travel = models.BooleanField(verbose_name='Disponibilidad para viajar')
    places = models.CharField(max_length=100, verbose_name='Número de plazas')
    published = models.DateTimeField(verbose_name='Fecha de Publicación', default=now)
    author = models.ForeignKey(User, verbose_name='Contacto', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    

    class Meta:
        verbose_name = 'vacante'
        verbose_name_plural = 'vacantes'
        ordering = ['-created']
    
    def __str__(self):
        return self.position
