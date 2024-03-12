from django import forms
from .models import PatientRecord, ServiceRequest


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
        'patient_id': forms.CharField(),
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
        'date_of_visit': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'name_of_guardian': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Guardian'}),
        'relation_with_guardian': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Relation with Guardian'}),
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
            'service_category': forms.Select(attrs={'class': 'form-control'}),
            'service_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'requested_by': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service_category'].widget.choices = self.Meta.model.SERVICE_CATEGORY_CHOICES