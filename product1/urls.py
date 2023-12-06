"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tienda import views as ap
import tienda.urls as API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(API)),
    path('api-auth',include('rest_framework.urls')),
    path('inicio/',ap.index,name="home"),
    path('registrar/',ap.reg_user,name='registrar'),
    path('login/',ap.iniciar_sesion,name="login"),
    path('logout/',ap.cerrar_sesion,name='logout'),
    path('add_provf/',ap.add_provf,name='add_provf'),
    path('proveedores/',ap.list_provf,name="proveedores"),
    path('add_frut/',ap.add_frut,name='add_frut'),
    path('frutas/',ap.list_frut,name='frutas'),
    path('add_cat/',ap.add_cat,name='add_cat'),
    path('categorias/',ap.list_cat,name='categorias'),
    path('sin_acceso/',ap.sin_acceso,name='sin_acceso'),
]
