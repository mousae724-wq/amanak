from django.db.models import Count
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ScanResult, Report, Feedback
from .serializers import ScanResultSerializer, ReportSerializer, FeedbackSerializer

class DashboardStatsView(APIView):
    """GET /api/dashboard/stats/ - Aggregated system statistics."""

    def get(self, request):
        agg = ScanResult.objects.values('status').annotate(total=Count('id'))
        counts = {item['status']: item['total'] for item in agg}

        return Response({
            'total_scans': ScanResult.objects.count(),
            'safe_links': counts.get('safe', 0),
            'suspicious_links': counts.get('suspicious', 0),
            'dangerous_links': counts.get('dangerous', 0),
            'total_reports': Report.objects.count(),
            'total_feedback': Feedback.objects.count(),
        })

class ScanListCreateView(generics.ListCreateAPIView):
    """GET / POST /api/dashboard/scans/ - List and create scan results."""

    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer

class ReportListCreateView(generics.ListCreateAPIView):
    """GET / POST /api/reports/ - List and create reports."""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class FeedbackListCreateView(generics.ListCreateAPIView):
    """GET / POST /api/feedback/ - List and create feedback."""

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer