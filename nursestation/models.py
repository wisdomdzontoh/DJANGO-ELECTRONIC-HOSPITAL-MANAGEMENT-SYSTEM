from django.db import models
from django.contrib.auth.models import User
from patient_records.models import PatientRecord
from services.models import Services


class NurseStation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    patient = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date_of_appointment = models.DateTimeField()  
    reason_of_appointment = models.TextField(max_length=255, default="none")
    appointment_created_at = models.DateTimeField(auto_now_add=True)
    SPO2 = models.CharField(max_length=50, default="none")
    respiratory_rate = models.CharField(max_length=50, default="none")
    pulse = models.CharField(max_length=50, default="none")
    RBS = models.CharField(max_length=50, default="none")
    weight = models.CharField(max_length=50, default="none")
    height = models.CharField(max_length=50, default="none")
    BP = models.CharField(max_length=50, default="none")
    temperature = models.CharField(max_length=50, default="none")
    status_of_appointment = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    

    def __str__(self):
        return f"{self.patient} - {self.status_of_appointment}"