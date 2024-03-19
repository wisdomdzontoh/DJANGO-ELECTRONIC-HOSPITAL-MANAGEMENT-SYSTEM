from django.db import models

class Conditions(models.Model):
    name_of_condition = models.CharField(max_length=50)
    ICD11_code = models.CharField(max_length=50)
    last_updated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name_of_condition}'