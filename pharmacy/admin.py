# pharmacy/admin.py
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Prescription

class PrescriptionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.clean()  # run CDS checks
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            self.message_user(request, f"CDS Alert: {e}", level="error")

admin.site.register(Prescription, PrescriptionAdmin)
