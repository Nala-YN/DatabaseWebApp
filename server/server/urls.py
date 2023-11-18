"""
URL configuration for server project.

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
from django.urls import path
from myApp import views as LoginView

urlpatterns = [
    path('api/register', LoginView.register),
    path('api/login', LoginView.login),
    path('api/upload', LoginView.upload),
    path('api/uploadsell', LoginView.uploadsell),
    path('api/uploadpost', LoginView.uploadpost),
    path('api/getallpost', LoginView.getallpost),
    path('api/getuserpost', LoginView.getuserpost),
    path('api/deletepost', LoginView.deletepost),
    path('api/getuserinfo', LoginView.getuserinfo)
]
