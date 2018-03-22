"""ejercicio9_6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url	
from django.contrib import admin
from . import views

urlpatterns = [		#considerar cualquier cosa como url/recurso y contemplar si falla urllib (entonces no seria url valida y no va a estar en la cache)
    url(r'^(.+)$', views.buscar),	#primer param: patrón de la url(. significa cualquier cosa, + significa al menos 1 elemento, * significa ninguno o uno), segundo param: función a la que quiero llamar
	url(r'^$', views.hola),
]
