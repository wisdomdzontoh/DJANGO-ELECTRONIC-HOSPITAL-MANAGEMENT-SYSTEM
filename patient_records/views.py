from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PatientRecord
from .forms import PatientRecordForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from datetime import datetime
import csv
import xlwt  # For Excel format
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from .models import PatientRecord, ServiceRequest
from .forms import PatientRecordForm, ServiceRequestForm




@login_required(login_url="authentication:my-login")
def view_all_patients(request):
    # Retrieve patient records sorted by date_of_visit
    patient_records = PatientRecord.objects.order_by('-date_of_visit').all()
    
    # Paginate the sorted patient records
    paginator = Paginator(patient_records, 10)
    page_number = request.GET.get('page')
    patient_records = paginator.get_page(page_number)
    
    return render(request, 'patient_records/view_all_patients.html', {'patient_records': patient_records})

@login_required(login_url="authentication:my-login") 
def view_patient(request, id):
    patient_record = PatientRecord.objects.get(pk=id)
    return render(request, 'patient_records/view_patient.html', {'patient_record': patient_record})


# Add a new patient record 
# Add a new patient record 
@login_required(login_url="authentication:my-login") 
def add(request):
    if request.method == 'POST':
        form = PatientRecordForm(request.POST)
        if form.is_valid():
            form.instance.last_updated = timezone.now()  # Set the last_updated field to the current date and time
            form.save()
            return render(request, 'patient_records/success.html')
   
    else:
        # Generate the patient ID
        generated_id = f'GHA-{get_random_string(length=8, allowed_chars="0123456789")}'
        # Prefill the form with the generated ID
        form = PatientRecordForm(initial={'patient_id': generated_id})
    return render(request, 'patient_records/add.html', {'form': form})


@login_required(login_url="authentication:my-login") 
def edit(request, id):
    patient_record = get_object_or_404(PatientRecord, pk=id)
    
    if request.method == 'POST':
        form = PatientRecordForm(request.POST, instance=patient_record)
        service_request_form = ServiceRequestForm(request.POST)
        
        if form.is_valid() and service_request_form.is_valid():
            form.save()
            service_request = service_request_form.save(commit=False)
            service_request.patient = patient_record
            service_request.save()
            # Redirect to the same page to clear form fields for adding another service request
            return redirect('edit_patient', id=id)
    else:
        form = PatientRecordForm(instance=patient_record)
        service_request_form = ServiceRequestForm()
    
    # Get service categories from the ServiceRequest model
    service_categories = ServiceRequest.SERVICE_CATEGORY_CHOICES
    
    return render(request, 'patient_records/edit.html', {
        'form': form,
        'service_request_form': service_request_form,
        'patient_record': patient_record,
        'service_categories': service_categories,
    })


#delete patient records
@login_required(login_url="authentication:my-login") 
def delete(request, id):
    if request.method == 'POST':
        patient_record = PatientRecord.objects.get(pk=id)
        patient_record.delete()
    return redirect('view_all_patients')


# dashboard function to display data
@login_required(login_url="authentication:my-login") 
def index(request):
    # Get the current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Query to count male and female patients for the current month
    gender_counts = PatientRecord.objects.filter(date_of_visit__month=current_month, date_of_visit__year=current_year) \
                        .values('gender') \
                        .annotate(count=Count('id'))

    # Query to count insured and non-insured patients for the current month
    client_status_counts = PatientRecord.objects.filter(date_of_visit__month=current_month, date_of_visit__year=current_year) \
                                .values('client_status') \
                                .annotate(count=Count('id'))

    # Prepare data for the bar chart
    gender_data = [{'gender': item['gender'], 'count': item['count']} for item in gender_counts]
    client_status_data = [{'client_status': item['client_status'], 'count': item['count']} for item in client_status_counts]

    return render(request, 'patient_records/index.html', {
        'gender_data': gender_data,
        'client_status_data': client_status_data
    })
    
    

#download data into excel or csv
@login_required(login_url="authentication:my-login")
def download_data(request, format):
    # Retrieve the data from the database
    patient_records = PatientRecord.objects.all()

    # Define the filename based on the format
    if format == 'csv':
        filename = 'patient_records.csv'
        content_type = 'text/csv'
    elif format == 'excel':
        filename = 'patient_records.xls'
        content_type = 'application/vnd.ms-excel'
    else:
        # Handle invalid format
        return HttpResponse("Invalid format", status=400)

    # Create the HttpResponse object with the appropriate content type
    response = HttpResponse(content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Write data to the response in the specified format
    if format == 'csv':
        writer = csv.writer(response)
        writer.writerow(['Patient ID', 'NHIS Number', 'Date of visit', 'First Name', 'Last Name', 
                         'Age', 'Phone', 'Occupation', 'Gender', 'Client Type', 'Client Status', 'Address', 
                         'Guardian Name', 'Guardian Relation', 'Guardian Contact'])
        for record in patient_records:
            writer.writerow([
                record.patient_id,
                record.NHIS_number,
                record.date_of_visit,
                record.first_name,
                record.last_name,
                record.age,
                record.phone,
                record.occupation,
                record.gender,
                record.client_type,
                record.client_status,
                record.address,
                record.name_of_guardian,
                record.relation_with_guardian,
                record.contact_of_guardian
            ])
    elif format == 'excel':
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Patient Records')
        row_num = 0
        columns = ['Patient ID', 'NHIS Number', 'Date of visit',  'First Name', 'Last Name', 'Age', 'Gender', 
                   'Phone', 'Occupation', 'Client Type', 'Client Status', 'Address', 'Guardian Name', 'Guardian Relation', 'Guardian Contact']
        for col_num, column in enumerate(columns):
            sheet.write(row_num, col_num, column)
        for record in patient_records:
            row_num += 1
            sheet.write(row_num, 0, record.patient_id)
            sheet.write(row_num, 1, record.NHIS_number)
            sheet.write(row_num, 2, record.date_of_visit)
            sheet.write(row_num, 3, record.first_name)
            sheet.write(row_num, 4, record.last_name)
            sheet.write(row_num, 5, record.age)
            sheet.write(row_num, 6, record.gender)
            sheet.write(row_num, 7, record.phone)
            sheet.write(row_num, 8, record.occupation)
            sheet.write(row_num, 9, record.client_type)
            sheet.write(row_num, 10, record.client_status)
            sheet.write(row_num, 11, record.address)
            sheet.write(row_num, 12, record.name_of_guardian)
            sheet.write(row_num, 13, record.relation_with_guardian)
            sheet.write(row_num, 14, record.contact_of_guardian)
        workbook.save(response)

    return response


# SERVICE REQUEST HANDLING
def add_service_request(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        service_category = request.POST.get('service_category')
        service_price = request.POST.get('service_price')
        requested_by = request.POST.get('requested_by')

        # Assuming you have a ForeignKey relationship between PatientRecord and ServiceRequest
        patient_record = PatientRecord.objects.get(patient_id=patient_id)

        # Create a new service request instance and save it
        service_request = ServiceRequest(
            service_category=service_category,
            service_price=service_price,
            Service_requested_by=requested_by
        )
        service_request.save()

        # Add the service request to the patient's records
        patient_record.service_requests.add(service_request)

    # Redirect to the edit page or any other appropriate page
    return redirect('edit_patient', id=patient_id)