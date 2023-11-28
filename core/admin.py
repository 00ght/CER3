from django.contrib import admin
from .models import Evento, Segmento, User
from django.contrib.auth.admin import UserAdmin

class EventoAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'fecha_inicio', 'fecha_termino', 'Tipo')
    filter_horizontal = ('Segmento',) 

class SegmentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class TipoUsuarioAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'segmento')
    fieldsets = UserAdmin.fieldsets + (
        ('Segmento', {'fields': ('segmento',)}),
    )

admin.site.register(Evento, EventoAdmin)
admin.site.register(Segmento, SegmentoAdmin)
admin.site.register(User,TipoUsuarioAdmin)

