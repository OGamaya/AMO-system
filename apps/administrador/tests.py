# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class AdministradorTestCase(TestCase):
    # Para verificar la integracion con CodeShip
    def test_echo_for_CI(self):
        """Animals that can speak are correctly identified"""
        print ("Ejecuta el test de Administrador")
        self.assertEqual('Modulo administrador', 'Modulo administrador')