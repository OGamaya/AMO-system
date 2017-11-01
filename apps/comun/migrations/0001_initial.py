# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-10-31 23:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('foto', models.ImageField(null=True, upload_to='images/finca')),
                ('descripcion', models.CharField(max_length=1000, null=True)),
                ('municipio', models.CharField(max_length=150)),
                ('ubicacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(null=True, upload_to='images/user')),
                ('descripcion', models.CharField(max_length=1000, null=True)),
                ('telefono', models.IntegerField(null=True)),
                ('auth_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_cooperativa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comun.Cooperativa')),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comun.Rol')),
            ],
        ),
        migrations.AddField(
            model_name='finca',
            name='id_usuario_productor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comun.Usuario'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='id_usuario_comprador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comun.Usuario'),
        ),
    ]
