from django.urls import path

from . import views

urlpatterns = [
    path('', views.reservations_home, name='reservations_home'),
    path('confirm/', views.reservation_confirm, name='reservation_confirm'),
    path('complete/', views.reservation_complete, name='reservation_complete'),
    path('json', views.json_view, name='json_view'),
]