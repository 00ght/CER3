from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Segmento(models.Model):
    id = models.BigAutoField(primary_key=True)
    SEGMENTO_CHOICES = [
        ('Comunidad USM', 'Comunidad USM'),
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
        ('Jefe de Carrera', 'Jefe de Carrera'),
    ]
    nombre = models.CharField(max_length=35, choices=SEGMENTO_CHOICES)

    def __str__(self)->str:
        return self.nombre

class User(AbstractUser):
    segmento=models.ForeignKey(Segmento,null=True, on_delete=models.CASCADE)
    '''def __str__(self) -> str:
        return self.segmento''' #con esto no deja crear usuarios

class Evento(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=False)
    fecha_termino = models.DateTimeField(auto_now_add=False)
    Titulo = models.CharField(max_length=55)
    Descripcion = models.CharField(max_length=105)
    TIPO_CHOICES = [
        ('V', 'Vacaciones'),
        ('F', 'Feriado'),
        ('S_A', 'Suspension de actividades'),
        ('S_A_PM', 'Suspension de actividades (PM)'),
        ('P', 'Periodo Lectivo'),
        ('S_E', 'Suspension de evaluaciones'),
        ('C', 'Ceremonia'),
        ('E', 'EDDA'),
        ('A', 'Ayudantias'),
        ('H', 'Hito Academico'),
        ('S', 'Secretaria Academica'),
        ('Q', 'QAI'),
    ]
    Tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    Segmento = models.ManyToManyField(Segmento, related_name='eventos')

    def __str__(self)->str:
        return self.Titulo

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['Titulo', 'Descripcion', 'Tipo', 'Segmento']

    Segmento = forms.ModelMultipleChoiceField(
        queryset=Segmento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

