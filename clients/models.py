from django.db import models

class Sensor(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField("Codigo del sensor", max_length=50, null=False, blank=False)
  fecha_creacion = models.DateTimeField("Fecha de creacion", auto_now=False, auto_now_add=True)

  class Meta:
    ordering = ['id']
    verbose_name = 'Sensor'
    verbose_name_plural = 'Sensors'

  def __str__(self):
    return self.nombre

class Lectura(models.Model):
  id = models.AutoField(primary_key=True)
  sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True, blank=True)
  lectura_sensor = models.FloatField("Lectura del sensor (Wh)", max_length=5, null=True, blank=True)
  fecha_sensado = models.DateTimeField("Fecha de medicion", auto_now=False, auto_now_add=True)

class Client(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField("Nombre",max_length=50, null=False, blank=False)
  apellidos = models.CharField("Apellidos",max_length=50, null=False, blank=False)
  numero_suministro = models.CharField("N° Suministro",max_length=50, null=True, blank=False)
  direccion = models.CharField("Dirección",max_length=100, null=False, blank=False)
  departamento = models.CharField("Departamento",max_length=100, null=False, blank=False)
  provincia = models.CharField("Provincia",max_length=50, null=False, blank=False)
  fecha_creacion = models.DateTimeField("Fecha de creacion", auto_now=False, auto_now_add=True)

  class Meta:
    ordering = ['id']
    verbose_name = 'Client'
    verbose_name_plural = 'Clients'

  def __str__(self):
    return str(self.numero_suministro)

class ElectricMeter(models.Model):
  id = models.AutoField(primary_key=True)
  numero_medidor = models.CharField("N° Medidor",max_length=50, null=False, blank=False)
  potencia = models.CharField("Potencia (kWh)",max_length=50, null=False, blank=True)
  acometida = models.CharField("Acometida",max_length=50, null=False, blank=True)
  client_id = models.OneToOneField(Client, on_delete=models.CASCADE, verbose_name="Cliente", null=True, blank=True)
  sensor_id = models.OneToOneField(Sensor, on_delete=models.SET_NULL, verbose_name="Sensor de medición", null=True, blank=True)
  fecha_creacion = models.DateTimeField("Fecha de creacion", auto_now=False, auto_now_add=True)
  state = models.BooleanField("Estado",default=True)

  class Meta:
    ordering = ['id']
    verbose_name = 'ElectricMeter'
    verbose_name_plural = 'ElectricMeters'

  def __str__(self):
    return self.numero_medidor
