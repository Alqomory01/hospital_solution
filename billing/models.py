from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class ServiceItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(ServiceItem, through='InvoiceItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=[('Pending','Pending'),('Paid','Paid'),('Cancelled','Cancelled')],
        default='Pending'
    )

    def __str__(self):
        return f"Invoice {self.id} for {self.patient}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service_item = models.ForeignKey(ServiceItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.service_item.name} x {self.quantity}"

class Payment(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(
        max_length=20,
        choices=[('Cash','Cash'),('Card','Card'),('Insurance','Insurance')]
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Invoice {self.invoice.id}"


# Create your models here.
