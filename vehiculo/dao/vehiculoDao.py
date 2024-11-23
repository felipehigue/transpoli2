
from vehiculo.models import Vehiculo


class vehiculoDAO:
    @staticmethod
    def obtener_todos():
        return Vehiculo.objects.all()

    @staticmethod
    def obtener_por_id(vehiculo_id):
        try:
            return Vehiculo.objects.get(id=vehiculo_id)
        except Vehiculo.DoesNotExist:
            return None

    @staticmethod
    def crear_vehiculo(nombre, email, activo=True):
        vehiculo = vehiculo(nombre=nombre, email=email, activo=activo)
        vehiculo.save()
        return vehiculo
    



def actualizar_vehiculo(vehiculo_id, tipo, ubicacion_actual, estado, kilometraje, sensor, conductor, mantenimiento_ruta_actual, ruta, reporte):
    try:
        vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        
        # Actualiza los campos del vehículo
        vehiculo.tipo = tipo
        vehiculo.ubicacion_actual = ubicacion_actual
        vehiculo.estado = estado
        vehiculo.kilometraje = kilometraje
        vehiculo.sensor = sensor
        vehiculo.conductor = conductor
        vehiculo.mantenimiento_ruta_actual = mantenimiento_ruta_actual
        vehiculo.ruta = ruta
        vehiculo.reporte = reporte
        
        # Guarda los cambios
        vehiculo.save()
        return vehiculo
    except Vehiculo.DoesNotExist:
        return None


@staticmethod
def eliminar_vehiculo(vehiculo_id):
        Vehiculo.objects.filter(id=vehiculo_id).delete()