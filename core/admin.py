from django.contrib import admin
from .models import ScanResult, Report, Feedback

@admin.register(ScanResult)
class ScanResultAdmin(admin.ModelAdmin):
    list_display = ('url', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('url',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_scans', 'safe_count', 'suspicious_count', 'dangerous_count', 'created_at')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating',)