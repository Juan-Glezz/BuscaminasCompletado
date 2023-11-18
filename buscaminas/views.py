from django.shortcuts import render
from .forms import tableForm
import random
from .buscaminas import Tablero

def index(req):
   return render(req, 'buscaminas/index.html')


def form_tablero(request):
    t_minas=None
    if request.method == 'POST':
        table_form = tableForm(request.POST)
        if table_form.is_valid():
            columna = int(table_form.cleaned_data['columna'])
            fila = int(table_form.cleaned_data['fila'])
            minas = int(table_form.cleaned_data['minas'])

            if minas <= (fila*columna) / 2:
                t_minas = Tablero(fila, columna, minas).muestraTablero()
    else:
        table_form = tableForm()

    if t_minas is not None:
        return render(request, 'buscaminas/muestraTablero.html', {'form': table_form, 'tablero': t_minas})
    else:
        return render(request, 'buscaminas/Tablero.html', {'form': table_form})
    
      
    


# Create your views here.