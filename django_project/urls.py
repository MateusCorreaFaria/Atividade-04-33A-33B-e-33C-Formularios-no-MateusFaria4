"""django_project URL Configuration

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
from django.urls import path
from app_mateus import views

urlpatterns = [
  path('', views.home, name = 'review'),
  path('admin/', admin.site.urls),
    path('carros',views.create_carros),   
    path('carros/update/<id>',views.update_carros),
    path('carros/delete/<id>',views.delete_carros),
    path('videogames',views.create_videogames),   
    path('videogames/update/<id>',views.update_videogames),
    path('videogames/delete/<id>',views.delete_videogames)
   
    

]
