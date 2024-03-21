from django.contrib import admin
from .models import ConsultingRoom, LabTest

# Register your models here.
admin.site.register(ConsultingRoom)


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ['lab_patient', 'type_of_lab_request', 'notes', 'time_requested']
    list_filter = ['type_of_lab_request', 'notes', 'time_requested']
    search_fields = ['lab_patient__patient', 'type_of_lab_request', 'notes']