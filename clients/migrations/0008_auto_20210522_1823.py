# Generated by Django 3.2.3 on 2021-05-22 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20210518_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectura',
            name='sensor_id',
        ),
        migrations.AddField(
            model_name='sensor',
            name='lectura_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.lectura'),
        ),
    ]
