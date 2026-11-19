from django.db import models

class ScanResult(models.Model):
    """Stores result of a single URL scan."""

    class Status(models.TextChoices):
        SAFE = 'safe', 'Safe'
         = 'suspicious', 'Suspicious'
        DANGEROUS = 'dangerous', 'Dangerous'

    url = models.URLField(max_length=2048)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SAFE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['status'])]

    def __str__(self):
        return f"{self.url} [{self.status}]"

class Report(models.Model):
    """Aggregated snapshot for dashboard reporting."""

    title = models.CharField(max_length=200)
    total_scans = models.PositiveIntegerField(default=0)
    safe_count = models.PositiveIntegerField(default=0)
    suspicious_count = models.PositiveIntegerField(default=0)
    dangerous_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Feedback(models.Model):
    """User feedback for dashboard quality tracking."""

    name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}/5"