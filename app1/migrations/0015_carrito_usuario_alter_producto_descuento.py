# Generated by Django 4.2.5 on 2023-11-22 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_producto_descuento_alter_usuario_nombre_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='descuento',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Descuento'),
        ),
    ]
