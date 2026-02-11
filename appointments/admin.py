from django.contrib import admin
from .models import *

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "date", "reason", "status")
    list_filter = ("patient", "doctor")
    search_fields =("patient", "date")


admin.site.register(Appointment, AppointmentAdmin)

# Register your models here.
