from django.urls import path
from usuarios import views 
from usuarios.views import actualizar_usuario, crear_usuario, eliminar_usuario 


urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/crear/', crear_usuario, name='crear_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/actualizar/<int:usuario_id>/', actualizar_usuario, name='actualizar_usuario'),
]
