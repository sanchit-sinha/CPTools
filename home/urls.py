"""CPTools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include
from home import views

urlpatterns = [
    path('', views.index , name = "home"),
    path('snippets', views.snippets , name = "snippets"),
    path('calculator', views.calulator , name = "calculator"),
    path('contact', views.contact , name = "contact"),
    path('cp_solutions', views.cp_solutions , name = "cp_solutions"),
    path('cp_solutions/codeforces', views.codeforces_submissions , name = "codeforces_submissions"),
]
