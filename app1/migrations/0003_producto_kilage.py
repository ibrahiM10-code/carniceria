# Generated by Django 4.2.5 on 2023-11-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='kilage',
            field=models.IntegerField(default=1, verbose_name='Kilage'),
        ),
    ]
