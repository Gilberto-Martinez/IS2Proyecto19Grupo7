# Generated by Django 2.2.6 on 2019-10-24 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionItem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateField(null=True),
        ),
    ]
