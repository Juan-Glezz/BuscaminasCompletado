from django import forms
from django.core.exceptions import ValidationError
class tableForm(forms.Form):
    fila = forms.IntegerField(label='Fila:',max_value=20, initial=2)
    columna = forms.IntegerField(label='Columna',max_value=15, initial=2)
    minas=forms.IntegerField(label='Minas', initial=1)
    
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
