from rest_framework import routers 
from .views import EventoViewSet 
from django.urls import path, include 

 
router = routers.DefaultRouter() #ayuda a q el API reconzca las url de miapp 
router.register('eventos', EventoViewSet) #llama a las url y las vincula con el viewSet, un register por cada viewSet (setra las urls de CarreraViewSet) 

urlpatterns = [ 

    path('', include(router.urls)), 

] 