# Generated by Django 2.2.6 on 2019-11-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionItem', '0010_auto_20191115_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cedula_identidad',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_proyecto',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='permiso',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.AlterField(
            model_name='lineabase',
            name='estado',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='lineabase',
            name='tarea',
            field=models.CharField(max_length=70),
        ),
    ]
