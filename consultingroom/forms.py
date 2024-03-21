from django import forms
from .models import PatientRecord, Conditions, ConsultingRoom, LabTest
from django.forms import DateInput


class ConsultingRoomForm(forms.ModelForm):
    class Meta:
        model = ConsultingRoom
        fields = '__all__'
        labels = {
            'patient': 'Select Patient name & ID',
            'date_of_diagnosis': 'date of diagnosis',
            'pregnant_patient': 'Is patient pregnant patient?',
            'provisional_diagnosis': 'provisional diagnosis',
            'principal_diagnosis': 'principal diagnosis',
            'principal_diagnosis_status_of_diagnosis': 'Status of principal diagnosis',
            'additional_diagnosis': 'Additional diagnosis',
            'additional_diagnosis_status_of_diagnosis': 'status of additional diagnosis',
            'other_diagnosis': 'other diagnosis not listed',
            'other_diagnosis_status_of_diagnosis': 'status of other diagnosis',
            'notes': 'Add clinical notes here',
        }
        
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date_of_diagnosis': forms.DateInput(attrs={'type': 'date'}),
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
    
    TYPE_OF_LAB_REQUEST_CHOICES = [
        ('RDT', 'RDT'),
        ('microscopy', 'Microscopy'),
        ('Hep_B', 'Hep B'),
    ]
    
    type_of_lab_request = forms.MultipleChoiceField(
        choices=TYPE_OF_LAB_REQUEST_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
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