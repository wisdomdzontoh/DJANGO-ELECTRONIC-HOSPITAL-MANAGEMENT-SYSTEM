from django.db import models

class Services(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    service_price = models.FloatField()
    last_updated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.service_name}'
