# Generated by Django 4.2.5 on 2023-11-21 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_producto_descuento_usuario_nombre_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='descuento',
        ),
    ]
