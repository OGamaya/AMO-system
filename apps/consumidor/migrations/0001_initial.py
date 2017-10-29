# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comun', '0001_initial'),
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('valor_total', models.FloatField()),
                ('cantidad_items', models.IntegerField()),
                ('fecha_entrega', models.DateTimeField(auto_now_add=True)),
                ('id_direccion_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comun.Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_compra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consumidor.Compra')),
                ('id_producto_catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.ProductoCatalogo')),
            ],
        ),
        migrations.CreateModel(
            name='MedioPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('id_usuario_comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comun.Usuario')),
            ],
        ),
    ]
