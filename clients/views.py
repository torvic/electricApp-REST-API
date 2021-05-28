from django.core.checks import messages
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
#from rest_framework import generics

from clients.serializers.general_serializers import SensorSerializer, LecturaSerializer, ClientSerializer, ElectricMeterSerializer 
from clients.models import Sensor, Lectura, Client, ElectricMeter

class SensorViewSet(viewsets.GenericViewSet):
  serializer_class = SensorSerializer
  queryset = Sensor.objects.all()

  # GET - Read all data
  def list(self, request):
    data = self.get_queryset()
    data_serializer = self.get_serializer(data, many=True)
    return Response(data_serializer.data)

  # POST - Create a data
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  # GET - Read one data
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
  
  # PUT - Update one data
  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  # DELETE - delete a data
  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response({'message':'delete successfully !'},status=status.HTTP_204_NO_CONTENT)
  
class LecturaViewSet(viewsets.ViewSet):

  #def list(self, request):
  #  queryset = Lectura.objects.all()
  #  serializer = LecturaSerializer(queryset, many=True)
  #  return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset_lectura = Lectura.objects.filter(sensor_id=pk)
    queryset_sensor = Sensor.objects.filter(id=pk)
    count = queryset_lectura.count()

    serializer_lectura = LecturaSerializer(queryset_lectura, many=True)
    serializer_sensor = SensorSerializer(queryset_sensor, many=True)

    return Response({'sensor': serializer_sensor.data,'lecturas': serializer_lectura.data, 'total_lecturas': count})

class ClientViewSet(viewsets.ModelViewSet):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()

  #def create(self, request, *args, **kwargs):
  #  serializer = self.get_serializer(data=request.data)
  #  serializer.is_valid(raise_exception=True)
  #  self.perform_create(serializer)
  #  headers = self.get_success_headers(serializer.data)
  #  return Response({'message':'Creado correctamente!'}, status=status.HTTP_201_CREATED, headers=headers)

class ElectricMeterViewSet(viewsets.ModelViewSet):
  serializer_class = ElectricMeterSerializer
  queryset = ElectricMeter.objects.all()
  

