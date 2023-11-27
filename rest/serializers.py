from rest_framework import serializers 
from core.models import Evento


class EventoSerializer(serializers.ModelSerializer): 

    class Meta: #clase con info de meta data, hace referencia a qué modelo ocupa 

        model = Evento
        fields = '__all__' #se muestran todos los datos del modelo, se hace un espejo totalmente igual 
        #fields = ['nombre', 'duracion'] #se muestran solo los campos nombre y duracion 
        #exclude = ['codigo'] #se muestan todos los campos menos codigo 