"""
URL configuration for polyconn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from polyconnmain.views import District, home, list_district, list_user, list_cafe, list_reservation


urlpatterns = [
    path("admin/", admin.site.urls),
    path('districts/', list_district, name='list_district'),
    path('', home, name='home'),
    path('user/', list_user, name='list_user'),
    path('cafe/', list_cafe, name='list_cafes'),
    path('reservation/', list_reservation, name='list_reservation')
]

