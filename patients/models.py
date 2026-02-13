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
class PatientNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='notes')
    doctor =models.ForeignKey('doctors.Doctor', on_delete=models.SET_NULL, null=True, related_name='notes' )
    note = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    version = models.IntegerField(default=1) 
    def __str__(self): 
        return f"Note for {self.patient.name} by {self.doctor.user.get_full_name()} (v{self.version})"