# Generated by Django 3.2.3 on 2021-05-22 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_auto_20210522_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='lectura_id',
        ),
        migrations.AddField(
            model_name='lectura',
            name='sensor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.sensor'),
        ),
    ]