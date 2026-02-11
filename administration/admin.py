from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ( (None, {'fields': ('role', 'department')}), ) 
    add_fieldsets = UserAdmin.add_fieldsets + ( (None, {'fields': ('role', 'department')}), )

    list_display= ['username', 'first_name', 'last_name', 'email', 'role', 'department']
    list_filter = ["role", "department"]
            
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_editable = ["description"]

class AuditLogAdmin(admin.ModelAdmin):
    list_display =["user","action", "timestamp", "details"]
    list_filter =["user", "details"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(AuditLog, AuditLogAdmin)
# Register your models here.
