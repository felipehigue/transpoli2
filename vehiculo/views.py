import json
from django.shortcuts import get_object_or_404, render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from vehiculo.dao import vehiculoDao
from vehiculo.dao.vehiculoDao import vehiculoDAO
from vehiculo.forms.vehiculo_forms import VehiculoForm
from vehiculo.models import Vehiculo


# Create your views here.



def listar_vehiculos(request):
    # Usamos el DAO para obtener todos los vehiculos
    vehiculos = vehiculoDAO.obtener_todos()
    print(f'vehiculos: {vehiculos}') 
    # Pasamos los vehiculos al template
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = vehiculoDAO.obtener_por_id(vehiculo_id)
    if vehiculo:
        vehiculo_data = {"id": vehiculo.id, "nombre": vehiculo.nombre, "email": vehiculo.email, "activo": vehiculo.activo}
        return JsonResponse(vehiculo_data)
    return JsonResponse({"error": "vehiculo no encontrado"}, status=404)

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            # Aquí se guarda el objeto Vehículo
            form.save()
            return redirect('listar_vehiculos')  # Cambia 'ruta_donde_redirigir' a la URL o nombre de la vista a la que quieres redirigir.
    else:
        form = VehiculoForm()
    return render(request, 'crear_vehiculos.html', {'form': form})


def eliminar_vehiculo(request, vehiculo_id):
    if request.method == 'POST':
        try:
            vehiculoDAO.eliminar_vehiculo(vehiculo_id)
            print(f"Vehículo eliminado: {vehiculo_id}")
            return redirect('listar_vehiculos')
        except Exception as e:
            print(f"Error al eliminar el vehículo: {e}")
            return HttpResponse(f"Error al eliminar el vehículo: {e}", status=500)
    return HttpResponse("Método no permitido", status=405)

# vehiculo/views.py



def actualizar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        ubicacion_actual = request.POST.get('ubicacion_actual')
        estado = request.POST.get('estado')
        kilometraje = request.POST.get('kilometraje')
        sensor = request.POST.get('sensor')
        conductor = request.POST.get('conductor')
        mantenimiento_ruta_actual = request.POST.get('mantenimiento_ruta_actual')
        ruta = request.POST.get('ruta')
        reporte = request.POST.get('reporte')

        try:
            # Llamar al método del DAO para actualizar el vehículo
            vehiculoDao.actualizar_vehiculo(vehiculo_id, tipo, ubicacion_actual, estado, kilometraje, sensor, conductor, mantenimiento_ruta_actual, ruta, reporte)
            return redirect('listar_vehiculos')
        except Exception as e:
            print(f"Error al actualizar el vehículo: {e}")
           

    return render(request, 'actualizar_vehiculo.html', {'vehiculo': vehiculo})
