from django.urls import path
from . import views

#la primera url llama a la vista index 
#La segunda tiene la ruta llamada tableroBusacminas donde se llama a la vista form_tablero
urlpatterns = [
    path('', views.index, name='index'),
    path("TableroBuscaminas" , views.form_tablero, name="TableroBuscaminas"),
   
]