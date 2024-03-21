from django.db import models
from patient_records.models import PatientRecord
from nursestation.models import NurseStation
from conditions.models import Conditions

class ConsultingRoom(models.Model):
    PREGNANT_PATIENT_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    STATUS_OF_DIAGNOSIS_CHOICES = [
        ('none', 'None'),
        ('new_case', 'New Case'),
        ('old_case', 'Old Case'),
    ]
    
    patient = models.ForeignKey(NurseStation, on_delete=models.CASCADE)
    date_of_diagnosis = models.DateField()
    pregnant_patient = models.CharField(max_length=3, choices=PREGNANT_PATIENT_CHOICES)
    provisional_diagnosis = models.ForeignKey(Conditions, related_name='provisional_diagnoses', on_delete=models.CASCADE, null=True, blank=True)
    principal_diagnosis = models.ForeignKey(Conditions, related_name='principal_diagnoses', on_delete=models.CASCADE, null=True, blank=True)
    principal_diagnosis_status_of_diagnosis = models.CharField(max_length=20, choices=STATUS_OF_DIAGNOSIS_CHOICES)
    additional_diagnosis = models.ForeignKey(Conditions, related_name='additional_diagnoses', on_delete=models.CASCADE, null=True, blank=True)
    additional_diagnosis_status_of_diagnosis = models.CharField(max_length=20, choices=STATUS_OF_DIAGNOSIS_CHOICES)
    other_diagnosis = models.CharField(max_length=100)
    other_diagnosis_status_of_diagnosis = models.CharField(max_length=20, choices=STATUS_OF_DIAGNOSIS_CHOICES)
    clinical_notes = models.TextField(default="none")
    
    
    def __str__(self):
        return f'{self.patient}'

# REQUEST LAB TEST
class LabTest(models.Model):
    TYPE_OF_LAB_REQUEST_CHOICES = [
        ('RDT', 'RDT'),
        ('microscopy', 'Microscopy'),
        ('Hep_B', 'Hep B'),
    ]
    
    lab_patient = models.ForeignKey(ConsultingRoom, on_delete=models.CASCADE)
    type_of_lab_request = models.CharField(max_length=10, choices=TYPE_OF_LAB_REQUEST_CHOICES)
    notes = models.TextField(default="none")
    time_requested = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Lab Test Record - {self.lab_patient}'
