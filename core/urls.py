from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, BookingViewSet, home, api_home

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', api_home, name='api-home'),
    path('api/', include(router.urls)),
]