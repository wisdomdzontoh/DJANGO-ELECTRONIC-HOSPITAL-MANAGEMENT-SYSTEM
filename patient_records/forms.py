from django import forms
from .models import PatientRecord, ServiceRequest
from django.forms import DateInput
class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = '__all__'
        labels = {
            'patient_id': 'Patient ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'other_names': 'Other Names',
            'age': 'Age',
            'phone': 'Phone',
            'gender': 'Gender',
            'age_group': 'Age group',
            'NHIS_number': 'NHIS Number',
            'client_type': 'Client Type',
            'client_status': 'Client Status',
            'occupation': 'Occupation',
            'level_of_education': 'Level of education',
            'address': 'Address',
            'date_of_visit': 'Date of Visit',
            'name_of_guardian': 'Name of Guardian',
            'relation_with_guardian': 'Relation with Guardian',
            'contact_of_guardian': 'Contact of Guardian',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
            'other_names': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'paul'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age_group': forms.Select(attrs={'class': 'form-control'}),
            'NHIS_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NHIS Number'}),
            'client_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Client Type'}),
            'client_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Client Status'}),
            'occupation': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Occupation'}),
            'level_of_education': forms.Select(attrs={'class': 'form-control', 'placeholder': 'level of education'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'date_of_visit': DateInput(attrs={'type': 'date'}),
            'name_of_guardian': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Guardian'}),
            'relation_with_guardian': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Relation with Guardian'}),
            'contact_of_guardian': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact of Guardian'}),
        }








class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        labels = {
            'service_category': 'Service Category',
            'service_price': 'Service Price',
            'requested_by': 'Requested By',
        }
        widgets = {
            'service_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
