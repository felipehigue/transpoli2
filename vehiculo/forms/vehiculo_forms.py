from django import forms
from django.core.exceptions import ValidationError
import re

from vehiculo.models import Vehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['tipo', 'placa', 'conductor', 'ruta']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'conductor': forms.TextInput(attrs={'class': 'form-control'}),
            'ruta': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Validación personalizada para la placa
    def clean_placa(self):
        placa = self.cleaned_data.get('placa')
        
        # Expresión regular para validar la placa: 3 letras seguidas de 3 números
        if not re.match(r'^[A-Za-z]{3}\d{3}$', placa):
            raise ValidationError("La placa debe tener 3 letras seguidas de 3 números.")
        
        return placa
