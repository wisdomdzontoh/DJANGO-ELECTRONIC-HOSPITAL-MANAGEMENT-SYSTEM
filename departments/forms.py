from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name_of_department', 'description']
        labels = {
            'name_of_department': 'Name of department',
            'description': 'Description',
        }
        
        widgets = {
            'name_of_department': forms.TextInput(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'describe the unit'}),
        }