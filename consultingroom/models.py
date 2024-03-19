from django.db import models
from patient_records.models import PatientRecord

class ConsultingRoom(models.Model):
    MORBIDITY_CONDITIONS_CHOICES = [
        ('uncomplicated malaria', 'uncomplicated malaria'),
        ('severe malaria', 'severe malaria'),
        ('Cholera', 'cholera'),
        
    ]
    
    STATUS_OF_DIAGNOSIS_CHOICES = [
        ('new case', 'new case'),
        ('old case', 'old case'),
        
    ]
    
    date_of_diagnosis = models.DateField()
    provisional_diagnosis = models.CharField(max_length=50)
    principal_diagnosis = models.CharField(max_length=50)
    


