from django.urls import path
from . import views

urlpatterns = [
    path('api', views.api, name="Api"),
    path('', views.home, name="home"),
    path('addbloginfo', views.addbloginfo, name="addbloginfo"),
]