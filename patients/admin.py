from django.contrib import admin

from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display= ['patient_id', 'name', 'dob',"contact_info", 'medical_history']
    search_fields = ['patient_id', 'name']
    readonly_fields = ['medical_history']
    list_filter = ['patient_id']

class PatientNoteAdmin(admin.ModelAdmin):
    list_display = ("patient","doctor","note", "created_at", "updated_at", "version")
    search_fields = ("patient", "note")
    list_filter = ['patient']
    readonly_fields =['created_at']
    ordering =("-created_at",)


admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientNote, PatientNoteAdmin)
# Register your models here.
