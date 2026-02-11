from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[
            ('Admin','Admin'),
            ('Doctor','Doctor'),
            ('Nurse','Nurse'),
            ('LabTech','LabTech'),
            ('Pharmacist','Pharmacist'),
            ('Patient','Patient')
        ]
    )
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    
    groups = models.ManyToManyField( Group, related_name="customuser_set", # avoids clash 
                                    blank=True ) 
    user_permissions = models.ManyToManyField( Permission, related_name="customuser_set", # avoids clash
                                                                                            blank=True )

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class AuditLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"

# Create your models here.
