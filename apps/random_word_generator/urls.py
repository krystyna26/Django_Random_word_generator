from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.nothing),
    url(r'^random_word/$', views.index),
    url(r'^random_word/generate$', views.generateRand),
    url(r'^random_word/reset$', views.reset) 
    ]