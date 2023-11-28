from django.shortcuts import render 
from rest_framework import viewsets 
from .serializers import EventoSerializer 
from core.models import Evento
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

@permission_classes([IsAdminUser])
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer