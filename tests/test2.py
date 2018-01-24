from django.test import TestCase
import unittest

class Smoketest(TestCase):

    def test_add(self):
        self.assertEqual(1+1,2,'ok')