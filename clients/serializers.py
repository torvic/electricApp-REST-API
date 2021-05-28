from clients.models import Sensor, ElectricMeter, Client

from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Sensor

class ElectricMeterSerializer(serializers.ModelSerializer):

  class Meta:
    model = ElectricMeter
    exclude = ('fecha_creacion',)

  def to_representation(self, instance):

    return {
      'id': instance.id,
      'numero_medidor': instance.numero_medidor,
      'potencia': instance.potencia,
      'acometida': instance.acometida,
      'sensor_id': instance.sensor_id.codigo if instance.sensor_id != None else '',
    }
    
class ClientSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Client
    exclude = ('state',)
  
  def to_representation(self, instance):
    return {
      'id': instance.id,
      'nombre': instance.nombre,
      'apellidos': instance.apellidos,
      'codigo_cliente': instance.codigo_cliente,
      'direccion': instance.direccion,
      'departamento': instance.departamento,
      'provincia': instance.provincia,
      'fecha_creacion': instance.fecha_creacion,
      'electric_meter': instance.medidor_id.numero_medidor
    }
  


