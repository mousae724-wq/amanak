from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/services/', views.services_list, name='services'),
    path('api/bookings/', views.bookings_list, name='bookings'),
]