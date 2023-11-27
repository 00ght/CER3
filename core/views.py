# views.py
from django.shortcuts import render
from .forms import EventoFilter
from .models import Evento, Segmento

def index(request):
    title = ""
    eventos = Evento.objects.all()

    form = EventoFilter(request.GET)
    if form.is_valid():
        segmentos_elegidos = form.cleaned_data.get('Segmento')
        tipos_elegidos = form.cleaned_data.get('Tipo')

        if segmentos_elegidos:
            eventos = eventos.filter(Segmento__in=segmentos_elegidos)

        if tipos_elegidos:
            eventos = eventos.filter(Tipo__in=tipos_elegidos)

    data = {
        "title": title,
        'segmentos_totales': Segmento.objects.count(),
        'segmentos': Segmento.objects.all(),
        'tipos': Evento.TIPO_CHOICES,
        'eventos': eventos,
        'form': form
    }

    return render(request, 'base.html', data)
