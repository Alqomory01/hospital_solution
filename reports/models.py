from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ReportType(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Daily Billing Summary"
    description = models.TextField(blank=True, null=True)
    query_definition = models.TextField()  # could store SQL/filters/parameters

    def __str__(self):
        return self.name


class GeneratedReport(models.Model):
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_generated = models.DateTimeField(auto_now_add=True)
    file_output = models.FileField(upload_to='reports/', blank=True, null=True)  # PDF/CSV export
    summary_text = models.TextField(blank=True, null=True)  # quick narrative summary

    def __str__(self):
        return f"{self.report_type.name} generated on {self.date_generated}"


class ReportAccessLog(models.Model):
    report = models.ForeignKey(GeneratedReport, on_delete=models.CASCADE)
    accessed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_accessed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.accessed_by} viewed {self.report}"


# Create your models here.
