# forms.py
from django import forms
from .models import Espacios

class EspacioForm(forms.ModelForm):
    class Meta:
        model = Espacios
        fields = ['name', 'descripcion', 'capacidad', 'imagen']  # Incluimos el campo de imagen

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre del espacio'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción'}),
            'capacidad': forms.NumberInput(attrs={'min': 1}),
            'imagen': forms.ClearableFileInput(),  # Widget para la carga de archivos
        }
