from django.shortcuts import render
from django.views import View
from .forms import EventoFilter
from .models import Evento, Segmento

def index(request):
    title = ""
    data = {
        "title": title,
        'segmentos_totales': Segmento.objects.count(),
        'segmentos': Segmento.objects.all(),
        'segmento_eleguido': request.GET.get('segmento')
    }

    return render(request, 'base.html', data)
