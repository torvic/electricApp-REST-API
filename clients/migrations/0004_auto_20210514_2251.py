# Generated by Django 3.2.3 on 2021-05-15 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_sensor_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electricmeter',
            name='sensor_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.sensor', verbose_name='Sensor de medición'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='codigo',
            field=models.CharField(max_length=50, verbose_name='Codigo del sensor'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='lectura',
            field=models.FloatField(blank=True, max_length=5, null=True, verbose_name='Lectura del medidor (Wh)'),
        ),
    ]
