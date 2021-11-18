from django.urls import path

from . import views

urlpatterns = [
    path('', views.locations_home, name='locations_home')
]