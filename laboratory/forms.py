from django import forms
from .models import TestTypes


class TestTypesForm(forms.ModelForm):
    class Meta:
        model = TestTypes
        fields = ['name_of_test', 'type_of_test', 'description']
        labels = {
            'name_of_test': 'Name of Test',
            'type_of_test': 'Type of test',
            'description': 'Description',
        }
        
        widgets = {
            'name_of_test': forms.TextInput(attrs={'placeholder':'e.g., Microscopy'}),
            'type_of_test': forms.TextInput(attrs={'placeholder':'e.g., Hematology'}),
            'description': forms.Textarea(attrs={'placeholder':'e.g., Give a description'}),
        }