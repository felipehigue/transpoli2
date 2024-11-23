from django.db import IntegrityError
from django.test import TestCase

# Create your tests here.
# test_forms.py
from django.test import TestCase
from usuarios.forms.usuario_forms import UsuarioForm
from usuarios.models import Usuario, Credenciales


class UsuarioCredencialesTest(TestCase):
    def setUp(self):
        # Crear un usuario para asociar con las credenciales
        self.usuario = Usuario.objects.create(rol='admin', nombre='felipe')
        self.credenciales = Credenciales.objects.create(
            usuario=self.usuario,
            email='example@gmail.com',
            contraseña='123'
        )

    def test_usuario_rol(self):
        """Verifica que el rol del usuario sea el esperado."""
        self.assertEqual(self.usuario.rol, 'admin')

    def test_usuario_nombre(self):
        """Verifica que el nombre del usuario sea el esperado."""
        self.assertEqual(self.usuario.nombre, 'felipe')

    def test_credenciales_usuario(self):
        """Verifica que las credenciales estén asociadas al usuario correcto."""
        self.assertEqual(self.credenciales.usuario, self.usuario)

    def test_credenciales_email(self):
        """Verifica que el email en las credenciales sea el esperado."""
        self.assertEqual(self.credenciales.email, 'example@gmail.com')

    def test_credenciales_contraseña(self):
        """Verifica que la contraseña en las credenciales sea la esperada."""
        self.assertEqual(self.credenciales.contraseña, '123')







