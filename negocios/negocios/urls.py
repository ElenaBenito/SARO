"""negocios URL Configuration

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

urlpatterns = [
	url(r'^$', 'foobar.views.barra'),		#añadido
	url(r'^aaa$', 'foobar.views.tresas'),	#añadido
	url(r'^(-?\d+)/suma/(-?\d+)$', 'foobar.views.calcular'),	#añadido, \d+-->uno o mas digitos, (\d+)-->se pasa como parametro a sumar, -?-->- esta 0 o una vez, .-->solo una vez,#-->0 p mas veces
    url(r'^admin/', include(admin.site.urls)),
]
