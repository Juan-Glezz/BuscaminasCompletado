from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("TableroBuscaminas" , views.form_tablero, name="TableroBuscaminas"),
   
]