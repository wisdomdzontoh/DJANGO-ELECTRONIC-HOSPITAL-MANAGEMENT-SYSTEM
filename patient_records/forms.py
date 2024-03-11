from django import forms
from .models import PatientRecord

class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = '__all__'
        labels = {
            'patient_id': 'Patient ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'phone': 'Phone',
            'gender': 'Gender',
            'age_group': 'Age group',
            'NHIS_number': 'NHIS Number',
            'client_type': 'Client Type',
            'client_status': 'Client Status',
            'occupation': 'Occupation',
            'address': 'Address',
            'date_of_visit': 'Date of Visit',
            'name_of_guardian': 'Name of Guardian',
            'relation_with_guardian': 'Relation with Guardian',
            'contact_of_guardian': 'Contact of Guardian',
        }

    widgets = {
        'patient_id': forms.NumberInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
        'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
        'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        'gender': forms.Select(attrs={'class': 'form-control'}),
        'age_group': forms.Select(attrs={'class': 'form-control'}),
        'NHIS_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NHIS Number'}),
        'client_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Type'}),
        'client_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Status'}),
        'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation'}),
        'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        'date_of_visit': forms.DateInput(attrs={'class': 'form-input', 'placeholder': 'Date of Visit', 'type': 'date'}),
        'name_of_guardian': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Guardian'}),
        'relation_with_guardian': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Relation with Guardian'}),
        'contact_of_guardian': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact of Guardian'}),
    }
