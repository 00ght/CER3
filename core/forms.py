from django import forms
from .models import Segmento, Evento

class EventoFilter(forms.Form):
    segmento= forms.ModelChoiceField(queryset=Segmento.objects.all(), required=False)
    tipo= forms.ChoiceField(choices=Evento.TIPO_CHOICES, required=False)