# Generated by Django 2.2.6 on 2019-10-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionItem', '0003_auto_20191028_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fase',
            field=models.CharField(choices=[('A', 'Analisis'), ('D', 'Diseño'), ('C', 'Codificación'), ('P', 'Prueba'), ('M', 'Mantenimiento')], max_length=13),
        ),
    ]
