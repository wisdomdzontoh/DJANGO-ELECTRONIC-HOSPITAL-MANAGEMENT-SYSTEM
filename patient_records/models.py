from django.db import models


class PatientRecord(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    AGE_GROUP_CHOICES = [
        ('0-28 days', '0-28 days'),
        ('1-11 months', '1-11 months'),
        ('1-4 years', '1-4 years'),
        ('5-9 years', '5-9 years'),
        ('10-14 years', '10-14 years'),
        ('15-17 years', '15-17 years'),
        ('18-19 years', '18-19 years'),
        ('20-34 years', '20-34 years'),
        ('35-49 years', '35-49 years'),
        ('50-59 years', '50-59 years'),
        ('60-69 years', '60-69 years'),
        ('70+ yrs & Above', '70 yrs & Above'),
    ]
    
    CLIENT_TYPE_CHOICES = [
        ('New client', 'new client'),
        ('old client', 'old client'),
    ]
    
    CLIENT_STATUS_CHOICES = [
        ('insured', 'insured'),
        ('non-insured', 'non-insured'),
    ]
    
    OCCUPATION_CHOICES = [
        ('unemployed', 'unemployed'),
        ('student', 'student'),
        ('farming', 'farming'),
        ('trading', 'trading'),
        ('artisan(hairdresser,seamstress)', 'artisan(hairdresser,seamstress)'),
        ('civil servant', 'civil servant'),
        ('others', 'others'),  
    ]
    
    RELATION_CHOICES = [
        ('parent', 'parent'),
        ('sibling', 'sibling'),
        ('uncle/aunt', 'uncle/aunt'), 
        ('grandparent', 'grandparent'),
        ('nephew/niece', 'nephew/niece'),
        ('other', 'other'),   
    ]
    
    EDUCATION_CHOICES = [
        ('no formal education', 'no formal education'),
        ('primary', 'primary'),
        ('JHS', 'JHS'), 
        ('SHS/Technical/Vocational', 'SHS/Technical/Vocational'),
        ('tertiary', 'tertiary'),
        ('other', 'other'),   
    ]


    patient_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50, default="none")
    age = models.FloatField()
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES)
    NHIS_number = models.CharField(max_length=30, default="none")
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE_CHOICES)
    client_status = models.CharField(max_length=20, choices=CLIENT_STATUS_CHOICES)
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)
    level_of_education = models.CharField(max_length=50, choices=EDUCATION_CHOICES, default="none")
    address = models.CharField(max_length=50, default="none")
    date_of_visit = models.DateField()
    name_of_guardian = models.CharField(max_length=50, default="none")
    relation_with_guardian = models.CharField(max_length=50, choices=RELATION_CHOICES)
    contact_of_guardian = models.CharField(max_length=50, default="none")

    def __str__(self):
        return f'{self.patient_id} - {self.last_name} {self.first_name}'


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
