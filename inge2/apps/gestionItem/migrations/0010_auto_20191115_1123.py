# Generated by Django 2.2.6 on 2019-11-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionItem', '0009_remove_usuario_contrasenha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(default='invitado', max_length=40, unique=True),
        ),
    ]
