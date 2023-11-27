from django.contrib import admin
from .models import Evento, Segmento, User

class EventoAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'fecha_inicio', 'fecha_termino', 'Tipo')
    filter_horizontal = ('Segmento',) 

class SegmentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Segmento, SegmentoAdmin)
admin.site.register(User)

