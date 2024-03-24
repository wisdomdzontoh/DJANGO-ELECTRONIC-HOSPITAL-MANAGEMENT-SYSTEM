from django import forms
from .models import HumanResource
from departments.models import Department  # Import the Department model from your department app
from django.forms import DateInput

class HumanResourceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Query all departments and populate the choices for the name_of_department field
        self.fields['name_of_department'].queryset = Department.objects.all()

    class Meta:
        model = HumanResource
        fields = '__all__'
        labels = {
            'name_of_staff': 'Name of staff',
            'gender': 'Gender',
            'qualification': 'Qualification',
            'name_of_department': 'Department name',
            'salary': 'Salary',
            'phone': 'Phone',
            'email': 'Email',
            'date_of_appointment': 'Date of appointment',
            'image_of_staff': 'Image of staff',
        }
        widgets = {
            'name_of_staff': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'qualification': forms.Select(attrs={'class': 'form-control'}),
            'name_of_department': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '200'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john@gmail.com'}),
            'date_of_appointment': DateInput(attrs={'type': 'date'}),
            'image_of_staff': forms.FileInput(),
        }
