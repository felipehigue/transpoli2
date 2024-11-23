from django import forms
from usuarios.models import Usuario 
from usuarios.models import Credenciales

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rol', 'nombre']
        
        widgets = {
            'rol': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona un rol'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
        }
        
        labels = {
            'rol': 'Selecciona un rol',
            'nombre': 'Nombre completo',
        }

# Formulario para Credenciales
class CredencialesForm(forms.ModelForm):
    class Meta:
        model = Credenciales
        fields = ['email', 'contraseña']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }

# Formulario combinado
class CrearUsuarioForm(forms.Form):
    # Campos del modelo Usuario
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}))
    rol = forms.ChoiceField(choices=[('admin', 'Admin'), ('conductor', 'Conductor'),('monitor','Monitor'),('gerente operaciones', 'Gerente operaciones')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    # Campos del modelo Credenciales
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

    # Método para guardar ambos modelos en la base de datos
    def guardar(self):
        usuario = Usuario.objects.create(
            nombre=self.cleaned_data['nombre'],
            rol=self.cleaned_data['rol']
        )
        Credenciales.objects.create(
            usuario=usuario,
            email=self.cleaned_data['email'],
            contraseña=self.cleaned_data['contraseña']
        )