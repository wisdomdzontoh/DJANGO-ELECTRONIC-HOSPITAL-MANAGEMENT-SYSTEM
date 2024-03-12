from django.db import models

class PatientRecord(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    AGE_GROUP_CHOICES = [
        ('0-28', '0-28 days'),
        ('1-11', '1-11 months'),
        ('1-4', '1-4 years'),
        ('5-9', '5-9 years'),
        ('10-14', '10-14 years'),
        ('15-17', '15-17 years'),
        ('18-19', '18-19 years'),
        ('20-34', '20-34 years'),
        ('35-49', '35-49 years'),
        ('50-59', '50-59 years'),
        ('60-69', '60-69 years'),
        ('70+', '70 yrs & Above'),
    ]
    
    CLIENT_TYPE_CHOICES = [
        ('New client', 'new client'),
        ('old client', 'old client'),
    ]
    
    CLIENT_STATUS_CHOICES = [
        ('insured', 'insured'),
        ('non-insured', 'non-insured'),
    ]

    patient_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.FloatField()
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES)
    NHIS_number = models.CharField(max_length=30, default="none")
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE_CHOICES)
    client_status = models.CharField(max_length=20, choices=CLIENT_STATUS_CHOICES)
    occupation = models.CharField(max_length=50, default="none")
    address = models.CharField(max_length=50, default="none")
    date_of_visit = models.DateField()
    name_of_guardian = models.CharField(max_length=50, default="none")
    relation_with_guardian = models.CharField(max_length=50, default="none")
    contact_of_guardian = models.CharField(max_length=50, default="none")

    def __str__(self):
        return f'PatientRecord: {self.first_name} {self.last_name}'


# SERVICE REQUESTS
class ServiceRequest(models.Model):
    SERVICE_CATEGORY_CHOICES = [
        ("OPD consultation", "OPD consultation"),
        ("Dental consultation", "Dental consultation"),
        ("Eye consultation", "Eye consultation"),
        ("ANC", "ANC"),
    ]

    patient = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    service_category = models.CharField(max_length=20, choices=SERVICE_CATEGORY_CHOICES)
    service_price = models.FloatField()
    requested_by = models.CharField(max_length=100)
    requested_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.service_category}"
