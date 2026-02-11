from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Medication(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Amoxicillin"
    description = models.TextField(blank=True, null=True)
    dosage_form = models.CharField(max_length=50)  # e.g., "Tablet", "Syrup"
    strength = models.CharField(max_length=50)  # e.g., "500mg"
    price = models.DecimalField(max_digits=10, decimal_places=2)  # for billing
    stock_quantity = models.PositiveIntegerField(default=0)  # inventory tracking

    def __str__(self):
        return f"{self.name} {self.strength} ({self.dosage_form})"


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    date_prescribed = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Prescription for {self.patient} by {self.doctor}"


class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    instructions = models.TextField()  # e.g., "Take 1 tablet twice daily"

    def __str__(self):
        return f"{self.medication.name} x {self.quantity}"


class DispenseRecord(models.Model):
    prescription_item = models.ForeignKey(PrescriptionItem, on_delete=models.CASCADE)
    date_dispensed = models.DateTimeField(auto_now_add=True)
    pharmacist = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='dispensed_by')

    def __str__(self):
        return f"Dispensed {self.prescription_item.medication.name} for {self.prescription_item.prescription.patient}"


# Create your models here.
