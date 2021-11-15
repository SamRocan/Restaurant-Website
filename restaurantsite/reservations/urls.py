from django.urls import path

from . import views

urlpatterns = [
    path('', views.reservations_home, name='reservations_home'),
    path('json', views.json_view, name='json_view')
]