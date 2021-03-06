"""Cremeria_Toscano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import logout_then_login
from django.conf.urls import url
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include(('Cremeria_Toscano_1.urls','Cremeria_Toscano_1'))),
    path('logout/', logout_then_login, name='logout'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/img/favicon.ico')),
]