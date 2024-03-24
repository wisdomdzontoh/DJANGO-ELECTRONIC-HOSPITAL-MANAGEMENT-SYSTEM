from django import forms
from .models import ConsultingRoom, LabTest
from nursestation.models import NurseStation
from conditions.models import Conditions
from patient_records.models import PatientRecord
from laboratory.models import TestTypes

class ConsultingRoomForm(forms.ModelForm):
    class Meta:
        model = ConsultingRoom
        fields = '__all__'
        
        labels = {
            'patient': 'Select Patient name & ID',
            'date_of_diagnosis': 'Date of diagnosis',
            'age': 'age',
            'age_type': 'Age in  (Days/Years/Months)',
            'age_group': 'Age group of patient',
            'gender': 'gender',
            'pregnant_patient': 'Is patient pregnant patient?',
            'provisional_diagnosis': 'Provisional diagnosis',
            'principal_diagnosis': 'Principal diagnosis',
            'principal_diagnosis_status_of_diagnosis': 'Status of principal diagnosis',
            'additional_diagnosis': 'Additional diagnosis',
            'additional_diagnosis_status_of_diagnosis': 'Status of additional diagnosis',
            'other_diagnosis': 'Other diagnosis not listed',
            'other_diagnosis_status_of_diagnosis': 'Status of other diagnosis',
            'clinical_notes': 'Add clinical notes here',
        }
        
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date_of_diagnosis': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'age_type': forms.RadioSelect(attrs={'class': 'form-control'}),
            'age_group': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'pregnant_patient': forms.RadioSelect(attrs={'class': 'form-control'}),
            'provisional_diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'principal_diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'principal_diagnosis_status_of_diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'additional_diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'additional_diagnosis_status_of_diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'other_diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
            'other_diagnosis_status_of_diagnosis': forms.Select(attrs={'class': 'form-control'}),
            'clinical_notes': forms.Textarea(),
        }

class LabTestForm(forms.ModelForm):


    class Meta:
        model = LabTest
        fields = ['lab_patient', 'type_of_lab_request', 'notes']
        labels = {
            'lab_patient': 'Select Patient name & ID',
            'type_of_lab_request': 'Add type of test (multiple)',
            'notes': 'Add additional information here',
        }
        
        widgets = {
            'lab_patient': forms.Select(attrs={'class': 'form-control'}),
            
            
            'notes': forms.Textarea(),
        }
