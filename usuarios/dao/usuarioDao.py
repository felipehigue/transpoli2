from usuarios.models import Usuario

class UsuarioDAO:
    @staticmethod
    def obtener_todos():
        return Usuario.objects.all()

    @staticmethod
    def obtener_por_id(usuario_id):
        try:
            return Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return None

    @staticmethod
    def crear_usuario(nombre, email, activo=True):
        usuario = Usuario(nombre=nombre, email=email, activo=activo)
        usuario.save()
        return usuario
    

    def actualizar_usuario(self, usuario_id, nombre, rol, email):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.nombre = nombre
            usuario.rol = rol
            usuario.email = email
            usuario.save()
            return usuario
        except Usuario.DoesNotExist:
            return None

    @staticmethod
    def eliminar_usua(usuario_id):
        Usuario.objects.filter(id=usuario_id).delete()