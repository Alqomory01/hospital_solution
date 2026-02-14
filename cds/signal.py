# cds/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from pharmacy.models import Prescription
from appointments.models import Appointment

@receiver(post_save, sender=Prescription)
def run_cds_checks(sender, instance, **kwargs):
    # Example: notify doctors app if a risky prescription is added
    print(f"CDS Alert: Check {instance.drug_name} for patient {instance.patient.name}")

@receiver(post_save, sender=Appointment) 
def create_followup_reminder(sender, instance, **kwargs): 
    if instance.follow_up_date: 
        print(f"Reminder: Follow-up for {instance.patient.name} on {instance.follow_up_date}")
