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
        #self.browser = webdriver.Chrome("C:\\Users\\Oscar Amaya\\Documents\\tmp\\delete\\chromedriver33.exe")
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        print ("Esta si")
        self.browser.get('http://localhost:8000')
        print ("abrio "+self.browser.title)

        self.assertIn('Productor', self.browser.title)