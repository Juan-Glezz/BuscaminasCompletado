from django.shortcuts import render
from .forms import tableForm
import random
from .buscaminas import Tablero

#Esta funcion lo que hace es devolver alindex
def index(req):
   return render(req, 'buscaminas/index.html')

#Esta funcion recibe el objeto request como parametro, dentro de esta se crea la 
# variable t_minas inicializada como el valor none, posteriomente se verifica si el metodo de solicitud es post
# si es valido se crea el fromulario table_form usando el formulario creado en forms(tableForm)
# despues se comprueba que el formulario es valido y si lo es se obtienen los valores columna, fila y minas del formulario
#posterioemte se realiza una comprobacion de que el numero de minas no sea mayor qu la mitad del nuemro totalde celdas
# si esto se cumple se crea el objeto de tablero llamado tablero, pasando las variables filas, columnas y minas
# y despues  con el metodo muestraTablero para obtener como sera el tablero
# porel contraio si no es el metodo post se crea un formulario vacion

#Por ultimo se hace la validacion de que t_mians no es none y si es cierto se renderiza
#el muestratablero.html pasando el formulario y el tablerocomo argumentos y 
# si no se renderiza el tablero.html pasando solo el formulario como argumento
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