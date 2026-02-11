from django.db import models

# Create your models here.
class Patient(models.Model): 
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    dob = models.DateField() 
    contact_info = models.TextField() 
    medical_history = models.TextField(blank=True) 
    def __str__(self): 
        return f"{self.name} (PAT{self.patient_id:04d})"