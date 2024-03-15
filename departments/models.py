from django.db import models

# Create your models here.
class Department(models.Model):
    name_of_department = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    last_updated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'department: {self.name_of_department}'