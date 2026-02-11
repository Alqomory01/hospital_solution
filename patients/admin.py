from django.contrib import admin

from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display= ['patient_id', 'name', 'dob',"contact_info", 'medical_history']
    search_fields = ['patient_id', 'name']
    readonly_fields = ['medical_history']
    list_filter = ['patient_id']

admin.site.register(Patient, PatientAdmin)

# Register your models here.
