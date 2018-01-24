import os
from django.test import TestCase
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUP(self):
        self.browser=webdriver.firefox()

    def TearDown(self):
        self.browser.quit()

    def test_can_start(self):
        #self.browser.get('http://localhost')
        self.browser.get('http://localhost:8000')
        self.assertIn('to-do',self.browser.title)
        self.fail('finish the test')

if __name__=="__main__":
    unittest.main(warnings='ignore')