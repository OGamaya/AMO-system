# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionComprador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_comprador', models.CharField(max_length=200)),
                ('id_comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comun.Usuario')),
            ],
        ),
    ]
