from django.test import TestCase

# Create your tests here.
# en tests.py
from django.test import TestCase
from django.urls import reverse
from .forms import vehiculo_forms
from .models import Vehiculo


class VehiculoFormTests(TestCase):

    def test_form_invalid_placa(self):
        # Datos inválidos para la placa (menos de 6 caracteres, o no sigue el patrón)
        data = {'placa': 'ABC12'}  # Invalid: less than 6 characters
        form = vehiculo_forms.VehiculoForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['placa'], ['La placa debe tener 3 letras seguidas de 3 números.'])

        data = {'placa': '123ABC'}  # Invalid: numbers before letters
        form = vehiculo_forms.VehiculoForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['placa'], ['La placa debe tener 3 letras seguidas de 3 números.'])

        data = {'placa': 'A1B2C3'}  # Invalid: letters and numbers mixed
        form = vehiculo_forms.VehiculoForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['placa'], ['La placa debe tener 3 letras seguidas de 3 números.'])

    def test_form_valid(self):
        # Datos válidos para la placa
        data = {'placa': 'ABC123'}  # Valid: 3 letters followed by 3 numbers
        form = vehiculo_forms.VehiculoForm(data)
        self.assertTrue(form.is_valid())
