from django import forms
from django.core.exceptions import ValidationError

#Esta clase hereda de la clase forms.Form,  en esta iniciamos las variable fila, columna y minas
class tableForm(forms.Form):
    fila = forms.IntegerField(label='Fila:',max_value=20, initial=2)
    columna = forms.IntegerField(label='Columna',max_value=15, initial=2)
    minas=forms.IntegerField(label='Minas', initial=1)
    
#El metodo clean lo utilizamos para validar los datos  integrados en el formulario, en nuestro
#caso comprueba que la cantidad de minas no sea superior a la mitad de las celdas totales, si es superior
# se muestra una excepcion  con un mensaje de error y a parte tambien comprueba que las minas no sean negativas
    def clean(self):
        cleaned_data = super().clean()
        fila = cleaned_data.get("fila")
        columna = cleaned_data.get("columna")
        minas = cleaned_data.get("minas")

        if minas:
            if minas > ((fila * columna) / 2):
                raise ValidationError(
                    "Has introducido una cantidad superior de minas impuestas."
                    )
            if minas<0:
                raise ValidationError(
                    "El numero de minas no puede ser negativo"
                )
        return cleaned_data
