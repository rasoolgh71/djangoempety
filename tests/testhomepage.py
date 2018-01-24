from django.test import TestCase
#from django.core.urlresolvers import resolve
from django.shortcuts import render
from task.views import home

class HomepageTest(TestCase):
    def test_root_url_home(self):
        found=render('')
        self.assertEqual(found.func,home)