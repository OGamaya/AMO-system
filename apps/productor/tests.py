from telnetlib import EC
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

_author_ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductorTestCase(TestCase):
    # Para verificar la integracion con CodeShip


    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Users\\Oscar Amaya\\Documents\\tmp\\delete\\chromedriver31.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000/productor/ver_ofertas')
        self.assertIn('Productor', self.browser.title)