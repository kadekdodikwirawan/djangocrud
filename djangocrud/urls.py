"""djangocrud URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from users import views as users
from loket import views as loket
from inistring import views as inistring
from fibonacci import views as fibonacci
from django.urls import path

urlpatterns = [
    path('users/', users.index, name='index'),
    path('fibonacci/', fibonacci.index, name='index'),
    path('loket/', loket.index, name='index'),
    path('inistring/', inistring.index, name='index'),
    path('admin/', admin.site.urls),
]
