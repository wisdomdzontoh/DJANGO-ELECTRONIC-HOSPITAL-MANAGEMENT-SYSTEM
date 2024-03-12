from django.contrib import admin
from .models import PatientRecord, ServiceRequest

# Register your models here.
admin.site.register(PatientRecord)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'service_category', 'service_price', 'requested_by', 'requested_on')

