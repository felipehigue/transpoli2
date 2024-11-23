
from django.urls import path

from vehiculo import views
from vehiculo.views import actualizar_vehiculo, crear_vehiculo, eliminar_vehiculo



urlpatterns = [

    path('vehiculo/', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculo/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('vehiculo/crear/', crear_vehiculo, name='crear_vehiculo'),
    path('vehiculo/eliminar/<int:vehiculo_id>/', eliminar_vehiculo, name='eliminar_vehiculo'),
    path('vehiculo/actualizar/<int:vehiculo_id>/', actualizar_vehiculo, name='actualizar_vehiculo'),
    
]