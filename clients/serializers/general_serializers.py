from rest_framework import serializers

from clients.models import Client, Sensor, Lectura, ElectricMeter


class LecturaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lectura
    exclude = ['sensor_id']

#class LecturaSensorSerializer(serializers.ModelSerializer):
#  sensor_id = serializers.StringRelatedField()
#  class Meta:
#    model = Lectura
#    fields = ['sensor_id']

class SensorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sensor
    exclude = ('fecha_creacion',)

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    exclude = ('fecha_creacion',)

class ElectricMeterSerializer(serializers.ModelSerializer):
  #sensor_id = serializers.StringRelatedField()
  class Meta:
    model = ElectricMeter
    exclude = ('fecha_creacion', 'state')

  def to_representation(self, instance):
    return {
      'id': instance.id,
      'numero_medidor': instance.numero_medidor,
      'potencia': instance.potencia,
      'acometida': instance.acometida,
      'client_id': instance.client_id.numero_suministro if instance.client_id != None else "", 
      'sensor_id': instance.sensor_id.nombre if instance.sensor_id != None else "",
    }