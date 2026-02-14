from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import path
from django.shortcuts import render
from django.db import models
from patients.models import Patient
from billing.models import Invoice
from laboratory.models import LabRequest
from .models import CustomUser, Department, AuditLog

class DashboardAdmin(admin.AdminSite):
    site_header = "Hospital Management System"
    site_title = "Hospital EMR Admin"
    index_title = "Dashboard"
    index_template = "dashboard/admin_index.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("dashboard/", self.admin_view(self.dashboard_view))
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        patient_count = Patient.objects.count()
        invoice_total = Invoice.objects.aggregate(total=models.Sum("total_amount"))["total"] or 0
        lab_pending = LabRequest.objects.filter(status="Pending").count()
        context = {
            "patient_count": patient_count,
            "invoice_total": invoice_total,
            "lab_pending": lab_pending,
        }
        return render(request, "dashboard/admin_dashboard.html", context)
    def index(self, request, extra_context=None): 
        patient_count = Patient.objects.count() 
        invoice_total = Invoice.objects.aggregate(total=models.Sum("total_amount"))["total"] or 0 
        lab_pending = LabRequest.objects.filter(status="Pending").count() 
        extra_context = extra_context or {} 
        extra_context.update({ 
            "patient_count": patient_count, 
            "invoice_total": invoice_total, 
            "lab_pending": lab_pending, }) 
        return super().index(request, extra_context=extra_context)

# Instantiate your custom admin site
admin_site = DashboardAdmin(name="hospital_admin")

# Register your models with this custom site
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('role', 'department')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('role', 'department')}),)
    list_display = ['username', 'first_name', 'last_name', 'email', 'role', 'department']
    list_filter = ["role", "department"]

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_editable = ["description"]

class AuditLogAdmin(admin.ModelAdmin):
    list_display = ["user", "action", "timestamp", "details"]
    list_filter = ["user", "details"]

admin_site.register(CustomUser, CustomUserAdmin)
admin_site.register(Department, DepartmentAdmin)
admin_site.register(AuditLog, AuditLogAdmin)

admin.site.register(CustomUser, CustomUserAdmin) 
admin.site.register(Department, DepartmentAdmin) 
admin.site.register(AuditLog, AuditLogAdmin)
