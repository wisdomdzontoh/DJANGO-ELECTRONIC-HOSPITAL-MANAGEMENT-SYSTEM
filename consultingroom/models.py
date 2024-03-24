from django.db import models
from nursestation.models import NurseStation
from conditions.models import Conditions
from laboratory.models import TestTypes
from patient_records.models import PatientRecord  # Import the PatientRecord model

class ConsultingRoom(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    AGE_GROUP_CHOICES = [
        ('0-28 days', '0-28 days'),
        ('1-11 months', '1-11 months'),
        ('1-4 years', '1-4 years'),
        ('5-9 years', '5-9 years'),
        ('10-14 years', '10-14 years'),
        ('15-17 years', '15-17 years'),
        ('18-19 years', '18-19 years'),
        ('20-34 years', '20-34 years'),
        ('35-49 years', '35-49 years'),
        ('50-59 years', '50-59 years'),
        ('60-69 years', '60-69 years'),
        ('70+ yrs & Above', '70 yrs & Above'),
    ]
    
    AGE_TYPE_CHOICES = [
        ('days', 'days'),
        ('months', 'months'),
        ('years', 'years'),        
    ]
    
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
    age = models.IntegerField(default=0)
    age_type = models.CharField(max_length=50, choices=AGE_TYPE_CHOICES, default="years")
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES, default="none")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="none")
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
    
    lab_patient = models.ForeignKey(ConsultingRoom, on_delete=models.CASCADE)
    type_of_lab_request = models.ForeignKey(TestTypes, on_delete=models.CASCADE)
    notes = models.TextField(default="none")
    time_requested = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Lab Test Record - {self.lab_patient} - {self.type_of_lab_request}'

# Define a function to retrieve the default age value from PatientRecord
def get_default_age():
    default_record = PatientRecord.objects.first()
    if default_record:
        return default_record.age
    else:
        return 0  # Return a default value if no records exist

# Update the default value of the age field to the value retrieved from PatientRecord
ConsultingRoom._meta.get_field('age').default = get_default_age


