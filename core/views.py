from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'core/home.html')

def services_list(request):
    return JsonResponse([], safe=False)

def bookings_list(request):
    return JsonResponse([], safe=False)