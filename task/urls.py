from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^show$', views.show, name='show'),
    url(r'^testjava$', views.testjave, name='testjava'),
    url(r'^email$',views.sendemail,name="email")
    #url(r'monitor$', views.get_monitoring, name='monitor'),
]