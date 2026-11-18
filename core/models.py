from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('confirmed', 'مؤكد'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service.name}"