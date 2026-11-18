from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service, Booking
from .serializers import ServiceSerializer, BookingSerializer

def home(request):
    return JsonResponse({
        "message": "اهلا بيك في أمانك ✅",
        "status": "شغال تمام",
        "api": "/api/services/"
    })

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Amanak API is working"})

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer