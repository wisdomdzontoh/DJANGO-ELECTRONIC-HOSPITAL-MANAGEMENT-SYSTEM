from django.db import models
from departments.models import Department  # Import the Department model from your department app

class HumanResource(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    QUALIFICATION_CHOICES = [
        ('shs', 'shs'),
        ('diploma', 'diploma'),
        ('bachelors degree', 'bachelors degree'),
    ]
    
    name_of_staff = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=50, choices=QUALIFICATION_CHOICES)
    name_of_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    date_of_appointment = models.DateField()
    image_of_staff = models.ImageField(upload_to='staff_images/')
    last_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name_of_staff} - {self.name_of_department}"
