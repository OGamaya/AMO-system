# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoOferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_definido', models.FloatField()),
                ('cantidad_definida', models.IntegerField()),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Catalogo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(null=True, upload_to='images')),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('foto', models.ImageField(null=True, upload_to='images')),
                ('catalogo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Catalogo')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(null=True, upload_to='images')),
                ('activo', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUnidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('abreviatura', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipoUnidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.TipoUnidad'),
        ),
        migrations.AddField(
            model_name='catalogooferta',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Producto'),
        ),
    ]
