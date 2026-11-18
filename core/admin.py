from django.contrib import admin
from .models import Service, Booking

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']
    list_filter = ['is_active']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'service', 'status', 'created_at']
    list_filter = ['status', 'service']
    search_fields = ['full_name', 'phone']