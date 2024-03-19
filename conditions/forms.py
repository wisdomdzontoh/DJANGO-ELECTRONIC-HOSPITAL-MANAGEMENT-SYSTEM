from django import forms
from .models import Conditions


class ConditionsForm(forms.ModelForm):
    class Meta:
        model = Conditions
        fields = ['name_of_condition', 'ICD11_code']
        labels = {
            'name_of_condition': 'Name of condition',
            'ICD11_code': 'ICD-11 Code',
        }
        
        widgets = {
            'name_of_condition': forms.TextInput(attrs={'placeholder':'e.g., Diabetes Mellitus'}),
            # 'ICD11_code': forms.Select(),  # This is the default, but I want to use a TextInput instead for user friendliness
            'ICD11_code': forms.TextInput(attrs={'placeholder': 'e.g., B40'}),  # ICD-11 code for diabetes mellitus
        }