# Generated by Django 4.2.5 on 2023-11-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_producto_kilage'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1, verbose_name='Stock'),
        ),
    ]
