from rest_framework import serializers
from .models import ScanResult, Report, Feedback

class ScanResultSerializer(serializers.ModelSerializer):
    """Serializer for scan results returned by dashboard."""

    class Meta:
        model = ScanResult
        fields = ['id', 'url', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']

class ReportSerializer(serializers.ModelSerializer):
    """Serializer for aggregated reports."""

    class Meta:
        model = Report
        fields = [
            'id',
            'title',
            'total_scans',
            'safe_count',
            'suspicious_count',
            'dangerous_count',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

class FeedbackSerializer(serializers.ModelSerializer):
    """Serializer for user feedback."""

    class Meta:
        model = Feedback
        fields = ['id', 'name', 'message', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']