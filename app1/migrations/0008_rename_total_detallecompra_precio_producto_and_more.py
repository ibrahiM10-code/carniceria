# Generated by Django 4.2.5 on 2023-11-20 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_detalleprecompra_detallecompra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallecompra',
            old_name='total',
            new_name='precio_producto',
        ),
        migrations.RenameField(
            model_name='detalleprecompra',
            old_name='total',
            new_name='precio_producto',
        ),
    ]
