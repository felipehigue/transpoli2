# Generated by Django 5.0.7 on 2024-11-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='ubicacion',
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='sensor',
            field=models.CharField(max_length=100),
        ),
    ]
