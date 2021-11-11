from django.urls import path

from . import views

urlpatterns = [
    path('', views.reservations_home, name='reservations_home')
]