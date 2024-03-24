from django.db import models

# Create your models here.
class TestTypes(models.Model):
    name_of_test = models.CharField(max_length=250)
    type_of_test = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    last_updated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name_of_test}'
    
    