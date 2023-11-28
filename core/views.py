from django.shortcuts import render
from datetime import date
from django.views import View
from datetime import date
from .forms import EventoFilter 
from .models import Evento, Segmento

def index(request):
    print("Entrando a views.index")
    title = ""
    segmento_usuario = None
    eventos = Evento.objects.filter(fecha_inicio__gte=date.today()).order_by('fecha_inicio') #Queryset general (todas las actividades)
    eventosPorSegmento = None  #Inicializar el queryset por segmento

    if request.user.is_authenticated:
        user = request.user
        segmento_usuario = user.segmento.nombre if (hasattr(user, 'segmento') and user.segmento) else None
        #Asignamos segmento segun usuario.
        if segmento_usuario == "Profesor":
            print("Es profesor") #Si el usuario tiene segmento = al nombre -> Filtra por nombre
            eventosPorSegmento = Evento.objects.filter(Segmento_nombre=segmento_usuario, fecha_inicio_gte=date.today()).order_by('fecha_inicio')
        elif segmento_usuario == "Jefe de Carrera": #Si el usuario tiene segmento = al nombre -> Filtra por nombre
            print("Es jefe de carrera")
            eventosPorSegmento = Evento.objects.filter(Segmento_nombre=segmento_usuario, fecha_inicio_gte=date.today()).order_by('fecha_inicio')

    else:
        print("Usuario no autenticado")
        #De lo contrario no filtra nada, y entrega las 3 actividades mas cercanas
   


    segmento_elegido = request.GET.getlist('segmento')
    tipo_elegido = request.GET.get('tipo')

    if segmento_elegido:
        if 'Segmento' not in segmento_elegido:
            eventos = eventos.filter(Segmento__nombre__in=segmento_elegido)

    if tipo_elegido:
        if 'Tipo' not in tipo_elegido:
            eventos = eventos.filter(Tipo__in=tipo_elegido)

    data = {
        "title": title,
        'segmentos_totales': Segmento.objects.count(),
        'segmentos': Segmento.objects.all(),
        'tipos': Evento.TIPO_CHOICES,
        'eventos': eventos,
        'segmento_elegido': segmento_elegido,
        'tipo_elegido': tipo_elegido,
        'eventosPorSegmento': eventosPorSegmento,
    }

    return render(request, 'base.html', data)