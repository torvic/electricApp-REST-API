from django.contrib import admin
from clients.models import Sensor, ElectricMeter, Client, Lectura

class SensorAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'fecha_creacion')

class LecturaAdmin(admin.ModelAdmin):
  list_display = ('id', 'sensor_id', 'lectura_sensor', 'fecha_sensado')

class ElectricMeterAdmin(admin.ModelAdmin):
  list_display = ('numero_medidor', 'potencia', 'acometida', 'client_id','sensor_id')

class ClientAdmin(admin.ModelAdmin):
  list_display = ('id','nombre', 'apellidos', 'numero_suministro', 'direccion', 'departamento', 'provincia')


admin.site.register(Sensor, SensorAdmin)
admin.site.register(ElectricMeter, ElectricMeterAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Lectura, LecturaAdmin)