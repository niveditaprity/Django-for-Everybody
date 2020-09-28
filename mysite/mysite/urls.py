"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [ # Change to ads.urls
 path('', include('home.urls')),
    path('admin/', admin.site.urls),
     path('ads/', include('ads.urls')),# Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep
path('menu/', include('menu.urls')),
    path('autos/', include('autos.urls')),
    path('hello/', include('hello.urls')),
    path('cats/', include('cats.urls')),
    path('polls/', include('polls.urls')),
]

