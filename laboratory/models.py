from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from django.core.exceptions import ValidationError

class LabTest(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Blood Sugar", "X-Ray"
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # for billing
    department = models.CharField(max_length=100, blank=True, null=True)  # e.g., "Pathology"

    def __str__(self):
        return self.name


class LabRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending','Pending'),('In Progress','In Progress'),('Completed','Completed')],
        default='Pending'
    )

    def __str__(self):
        return f"{self.test.name} for {self.patient}"


class LabResult(models.Model):
    request = models.OneToOneField(LabRequest, on_delete=models.CASCADE)
    result_text = models.TextField()  # narrative or structured result
    file_upload = models.FileField(upload_to='lab_results/', blank=True, null=True)  # optional PDF/image
    date_completed = models.DateTimeField(auto_now_add=True)
    verified_by = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_results')

    def clean(self): 
        if self.test_name == "Blood Sugar" and self.value > 200:
            raise ValidationError(f"Critical Alert: {self.patient.name} has high blood sugar ({self.value}).")
    def __str__(self):
        return f"Result for {self.request.test.name} ({self.request.patient})"


# Create your models here.
