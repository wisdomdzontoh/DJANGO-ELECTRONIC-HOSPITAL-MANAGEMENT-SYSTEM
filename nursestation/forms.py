from django import forms
from .models import NurseStation


class NurseStationForm(forms.ModelForm):
    class Meta:
        model = NurseStation
        fields = ['patient', 'doctor', 'type_of_service', 'date_of_appointment', 'status_of_appointment', 'reason_of_appointment', 
                  'SPO2', 'respiratory_rate', 'pulse', 'RBS', 'weight', 'height', 'BP', 'temperature' ]
        
        labels = {
            'patient' : 'Patient ID', 
            'doctor': 'doctor', 
            'type_of_service': 'Type of service',
            'date_of_appointment': 'date of appointment', 
            'status_of_appointment': 'status of appointment', 
            'reason_of_appointment': 'reason of appointment', 
            'SPO2': 'SPO2', 
            'respiratory_rate': 'respiratory rate', 
            'pulse': 'pulse', 
            'RBS': 'RBS', 
            'weight': 'weight', 
            'height': 'height', 
            'BP': 'BP', 
            'temperature': 'temperature',
        }
        widget = {
            'patient': forms.Select(attrs={'class': 'form-control'}), 
            'doctor': forms.Select(attrs={'class': 'form-control'}), 
            'type_of_service': forms.Select(attrs={'class': 'form-control'}),
            'date_of_appointment': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime'}), 
            'status_of_appointment': forms.Select(attrs={'class': 'form-control'}), 
            'reason_of_appointment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'eg: headache, cough'}), 
            'SPO2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
            'respiratory_rate': forms.TextInput(attrs={'class': 'form-control'}), 
            'pulse': forms.TextInput(attrs={'class': 'form-control'}), 
            'RBS': forms.TextInput(attrs={'class': 'form-control'}), 
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), 
            'BP': forms.TextInput(attrs={'class': 'form-control'}), 
            'temperature': forms.TextInput(attrs={'class': 'form-control'}),
        }