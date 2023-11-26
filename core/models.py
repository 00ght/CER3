from django import forms
from django.db import models
from django.contrib.auth.models import User

class Segmento(models.Model):
    SEGMENTO_CHOICES = [
        ('Comunidad USM', 'Comunidad USM'),
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
        ('Jefe de Carrera', 'Jefe de Carrera'),
    ]
    nombre = models.CharField(max_length=35, choices=SEGMENTO_CHOICES)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateTimeField(auto_now_add=True)
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

    def __str__(self):
        return self.Titulo

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['Titulo', 'Descripcion', 'Tipo', 'Segmento']

    Segmento = forms.ModelMultipleChoiceField(
        queryset=Segmento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
