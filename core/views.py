from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return JsonResponse({
        "message": "السيستم يعمل الان بنجاح",
        "status": "online",
        "api": "/api/services/",
        "admin": "/admin/"
    })

def services_list(request):
    return JsonResponse({
        "services": []
    })

def bookings_list(request):
    return JsonResponse({
        "bookings": []
    })