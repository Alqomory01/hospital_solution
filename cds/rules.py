# cds/rules.py
from django.core.exceptions import ValidationError

def check_allergy(patient, drug_name):
    if patient.allergies and drug_name.lower() in patient.allergies.lower():
        raise ValidationError(f"Alert: {patient.name} is allergic to {drug_name}!")

def check_duplicate_prescriptions(patient, drug_name):
    if patient.prescription_set.filter(drug_name__iexact=drug_name).exists():
        raise ValidationError(f"Duplicate prescription detected for {drug_name}.")
