from django.db import models
from patients.models import Patient 
from doctors.models import Doctor 

class Appointment(models.Model): 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    date = models.DateTimeField() 
    reason = models.TextField() 
    status = models.CharField( max_length=20, choices=[('Scheduled','Scheduled'),('Completed','Completed'),('Cancelled','Cancelled')] )
    follow_up_date = models.DateTimeField(null=True, blank=True) 

    
    def __str__(self): 
        return f"{self.patient} with {self.doctor} on {self.date}"

# Create your models here.
