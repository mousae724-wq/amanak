from django.urls import path
from .views import (
    DashboardStatsView,
    ScanListCreateView,
    ReportListCreateView,
    FeedbackListCreateView,
)

urlpatterns = [
    path('api/dashboard/stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('api/dashboard/scans/', ScanListCreateView.as_view(), name='scan-list'),
    path('api/reports/', ReportListCreateView.as_view(), name='report-list'),
    path('api/feedback/', FeedbackListCreateView.as_view(), name='feedback-list'),
]