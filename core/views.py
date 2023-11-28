from django.shortcuts import render
from django.views import View
from .forms import EventoFilter
from .models import Evento, Segmento

def index(request):
    print(request.GET)

    title = ""
    eventos = Evento.objects.all()

    segmento_elegido = request.GET.getlist('segmento')
    tipo_elegido = request.GET.get('tipo[]')

    if segmento_elegido:
        eventos = eventos.filter(Segmento__nombre__in=segmento_elegido)

    if tipo_elegido:
        eventos = eventos.filter(Tipo=tipo_elegido)

    data = {
        "title": title,
        'segmentos_totales': Segmento.objects.count(),
        'segmentos': Segmento.objects.all(),
        'tipos': Evento.TIPO_CHOICES,
        'eventos': eventos,
        'segmento_elegido': segmento_elegido,
        'tipo_elegido': tipo_elegido,
    }

    return render(request, 'base.html', data)
