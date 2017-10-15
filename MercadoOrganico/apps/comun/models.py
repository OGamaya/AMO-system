# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
       return "%s" % (self.nombre)

class Cooperativa(models.Model):
    ciudad = models.CharField(max_length=50)

    def __unicode__(self):
       return "%s" % (self.ciudad)

class Usuario(models.Model):
    foto = models.ImageField(upload_to='images/user',null=True)
    descripcion = models.CharField(max_length=1000,null=True)
    telefono = models.IntegerField(null=True)
    direccion = models.CharField(max_length=200)
    auth_user_id = models.ForeignKey(User, null = False)

    def __unicode__(self):
       return "%s" % (self.auth_user_id.first_name +  " " + self.auth_user_id.last_name)

    def natural_key(self):
        return (self.auth_user_id.first_name +  " " + self.auth_user_id.last_name)

class DireccionComprador(models.Model):
    direccion_comprador = models.CharField(max_length=200)
    id_comprador = models.ForeignKey(Usuario, null=False)

