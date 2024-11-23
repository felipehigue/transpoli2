import json
from django.shortcuts import get_object_or_404, render,redirect

from usuarios.models import Usuario
from django.views.decorators.csrf import csrf_exempt
from .forms.usuario_forms import CrearUsuarioForm
from django.http import JsonResponse
from usuarios.dao.usuarioDao import UsuarioDAO


# Create your views here.



def listar_usuarios(request):
    # Usamos el DAO para obtener todos los usuarios
    usuarios = UsuarioDAO.obtener_todos()
    print(f'Usuarios: {usuarios}') 
    # Pasamos los usuarios al template
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    usuario = UsuarioDAO.obtener_por_id(usuario_id)
    if usuario:
        usuario_data = {"id": usuario.id, "nombre": usuario.nombre, "email": usuario.email, "activo": usuario.activo}
        return JsonResponse(usuario_data)
    return JsonResponse({"error": "Usuario no encontrado"}, status=404)

def crear_usuario(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.guardar()  # Guarda el Usuario y sus Credenciales
            return redirect('listar_usuarios')  # O redirige a una página de éxito
    else:
        form = CrearUsuarioForm()

    return render(request, 'crear_usuarios.html', {'form': form})


def eliminar_usuario(request, usuario_id):
    print(f"Intentando eliminar usuario con ID: {usuario_id}")
    if request.method == 'POST':
        usuario = get_object_or_404(Usuario, id=usuario_id)
        print(f"Usuario encontrado: {usuario}")
        usuario.delete()
        print(f"Usuario eliminado: {usuario_id}")
        return redirect('listar_usuarios')
    print("Método no permitido")


@csrf_exempt
def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        # Procesar datos enviados en el formulario
        nombre = request.POST.get('nombre')
        rol = request.POST.get('rol')
        email = request.POST.get('email')

        # Actualizar el usuario
        usuario.nombre = nombre
        usuario.rol = rol
        usuario.email = email
        usuario.save()

        # Redirigir a la lista de usuarios
        return redirect('listar_usuarios')

    # Renderizar el formulario para editar el usuario
    return render(request, 'actualizar_usuarios.html', {'usuario': usuario, 'usuario_id': usuario_id})
    