# forms.py
from django import forms
from .models import Evento, Segmento

class EventoFilter(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['Segmento', 'Tipo']

    Segmento = forms.ModelMultipleChoiceField(
        queryset=Segmento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    Tipo = forms.ChoiceField(choices=Evento.TIPO_CHOICES, required=False)
