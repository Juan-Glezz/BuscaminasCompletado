from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import tableForm
from django.shortcuts import render, get_object_or_404
import random
from django.shortcuts import render

def index(req):
   return render(req, 'buscaminas/index.html')


def form_tablero(request):
    if request.method == 'POST':
        table_form = tableForm(request.POST)
        table_form_v = tableForm()
        if table_form.is_valid():
           
            columna = int(table_form.cleaned_data['columna'])
            fila = int(table_form.cleaned_data['fila'])
            minas = int(table_form.cleaned_data['minas'])
           
            filas_list = range(fila)
            columnas_list = range(columna)
            
            return render(request, 'buscaminas/muestraTablero.html', {'columna': columnas_list , "fila": filas_list , "table_form":table_form_v})
    else:
        table_form = tableForm()

    return render(request, 'buscaminas/Tablero.html', {'table_form': table_form})
      
    


# Create your views here.