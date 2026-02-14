# doctors/models.py
from django.db import models
from django.conf import settings  # to link with your CustomUser
from django.core.exceptions import ValidationError

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} ({self.specialization})"
    
class Encounter(models.Model): 
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE) 
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE) 
    notes = models.TextField() 
    def clean(self): 
        if self.patient.age > 50: raise ValidationError(f"Prompt: Consider colon cancer screening for {self.patient.name}.")


# Create your models here.
