# Generated by Django 4.2.5 on 2023-11-28 00:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_cajero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cajero',
            name='fecha_contratacion',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de contratacion'),
        ),
    ]