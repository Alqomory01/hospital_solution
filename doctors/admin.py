from django.contrib import admin
from .models import Doctor


class DoctorAdmin(admin.ModelAdmin): 
    list_display = ('get_full_name', 'specialization', 'license_number', 'phone', 'email', 'department') 
    search_fields = ('user__first_name', 'user__last_name', 'specialization', 'license_number') 
    list_filter = ('specialization', 'department') 

    def get_full_name(self, obj): 
        return f"{obj.user.first_name} {obj.user.last_name}" 
    get_full_name.short_description = 'Name' 
    
    
admin.site.register(Doctor, DoctorAdmin)
# Register your models here.
