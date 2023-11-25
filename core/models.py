from django import forms
from django.db import models
from django.contrib.auth.models import User

class Segmento(models.Model):
    SEGMENTO_CHOICES = [
        ('C_USM', 'Comunidad USM'),
        ('E', 'Estudiante'),
        ('P', 'Profesor'),
        ('J', 'Jefe de Carrera'),
    ]
    nombre = models.CharField(max_length=35, choices=SEGMENTO_CHOICES)

    def __str__(self) -> str:
        return self.nombre

class Evento(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateTimeField(auto_now_add=True)
    Titulo = models.CharField(max_length=55)
    Descripcion = models.CharField(max_length=105)
    TIPO_CHOICES = [
        ('V', 'Vacaciones'),
        ('F', 'Feriado'),
        ('S_A', 'Suspension_de_actividades'),
        ('S_A_PM', 'Suspension_de_actividades_PM'),
        ('P', 'Periodo_Lectivo'),
        ('S_E', 'Suspension_de_evaluaciones'),
        ('C', 'Ceremonia'),
        ('E', 'EDDA'),
        ('A', 'Ayudantias'),
        ('H', 'Hito_Academico'),
        ('S', 'Secretaria_Academica'),
        ('Q', 'QAI'),
    ]
    Tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    Segmento = models.ManyToManyField(Segmento, related_name='eventos')

    def __str__(self) -> str:
        return self.Titulo

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['fecha_inicio', 'fecha_termino', 'Titulo', 'Descripcion', 'Tipo', 'Segmento']

    Segmento = forms.ModelMultipleChoiceField(
        queryset=Segmento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
