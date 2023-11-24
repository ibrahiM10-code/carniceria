# Generated by Django 4.2.5 on 2023-11-21 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_detallecompra_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descuento',
            field=models.IntegerField(blank=True, null=True, verbose_name='Descuento'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(default='username', max_length=50, unique=True, verbose_name='Nombre de usuario (distinto al nombre anterior)'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombres'),
        ),
    ]