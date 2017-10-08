# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Catalogo(models.Model):
    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False)

class TipoUnidad(models.Model):
    nombre = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=5)

    def __unicode__(self):
       return "%s" % (self.abreviatura)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
       return "%s" % (self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='images', null=True)
    activo = models.BooleanField(default=False, null=False)
    tipoUnidad = models.ForeignKey(TipoUnidad, null=False)
    categoria = models.ForeignKey(Categoria, null=False)

    def __unicode__(self):
       return "%s" % (self.nombre)

class CatalogoOferta(models.Model):
    precio_definido = models.FloatField()
    cantidad_definida = models.IntegerField()
    catalogo = models.ForeignKey(Catalogo, null=True)
    producto = models.ForeignKey(Producto, null=True)