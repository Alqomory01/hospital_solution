from django.contrib import admin
from .models import *

class ReportTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ("name",)

class GeneratedReportAdmin(admin.ModelAdmin):
    list_display = ("report_type","generated_by","date_generated","file_output",)
    list_filter = ("report_type", "date_generated")
    search_fields = ("report_type__name", "summary_text")
    readonly_fields = ("date_generated",)
    ordering = ("-date_generated",)

class ReportAccessLogAdmin(admin.ModelAdmin):
    list_display = ("report","accessed_by","date_accessed")
    list_filter = ("date_accessed",)
    search_fields = ("report__report_type__name","accessed_by__username")
    readonly_fields = ("date_accessed",)
    ordering = ("-date_accessed",)



admin.site.register(ReportType, ReportTypeAdmin)
admin.site.register(GeneratedReport, GeneratedReportAdmin)
admin.site.register(ReportAccessLog,ReportAccessLogAdmin)

# Register your models here.
