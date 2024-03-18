from django import forms
from .models import Services


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['service_name', 'description', 'service_price']
        labels = {
            'service_name': 'Name of service',
            'description': 'Description',
            'service_price': 'Price'
        }
        
        widgets = {
            'service_name': forms.TextInput(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'describe service here'}),
            'price': forms.NumberInput(),
        }

