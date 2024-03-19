from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PatientRecord
from .forms import PatientRecordForm, ServiceRequestForm
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
from .models import PatientRecord
from django.db.models import Count
from django.db import connection
from django.db import OperationalError



# VIEW ALL PATIENT IN A TABLE
@login_required(login_url="authentication:my-login")
def view_all_patients(request):
    # Retrieve patient records sorted by date_of_visit
    patient_records = PatientRecord.objects.order_by('-date_of_visit').all()
    
    # Paginate the sorted patient records
    paginator = Paginator(patient_records, 10)
    page_number = request.GET.get('page')
    patient_records = paginator.get_page(page_number)
    
    return render(request, 'patient_records/view_all_patients.html', {'patient_records': patient_records})


# VIEW A PATIENT PROFILE
@login_required(login_url="authentication:my-login") 
def view_patient(request, id):
    patient_record = PatientRecord.objects.get(pk=id)
    return render(request, 'patient_records/view_patient.html', {'patient_record': patient_record})


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
        generated_id = f'GHA-{get_random_string(length=8, allowed_chars="0123456789")}/24'
        # Prefill the form with the generated ID
        form = PatientRecordForm(initial={'patient_id': generated_id})
    return render(request, 'patient_records/add.html', {'form': form})


# EDIT AND UPDATE PATIENT INFO (I AM NOT TOUCHING IT AGAIN)
@login_required(login_url="authentication:my-login") 
def edit(request, id):
    patient_record = get_object_or_404(PatientRecord, pk=id)
    
    if request.method == 'POST':
        form = PatientRecordForm(request.POST, instance=patient_record)
        
        if form.is_valid():
            form.save()
            return render(request, 'patient_records/update-success.html')
    else:
        form = PatientRecordForm(instance=patient_record)
    
    return render(request, 'patient_records/edit.html', {
        'form': form,
        'patient_record': patient_record,
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


# ADD SERVICE REQUEST
@login_required(login_url="authentication:my-login") 
def add_service_request(request, id):
    patient_record = get_object_or_404(PatientRecord, pk=id)
    
    if request.method == 'POST':
        service_request_form = ServiceRequestForm(request.POST)
        
        if service_request_form.is_valid():
            service_request = service_request_form.save(commit=False)
            service_request.patient = patient_record
            service_request.save()
            return redirect('edit', id=id)
    else:
        service_request_form = ServiceRequestForm()
    
    return render(request, 'patient_records/add_service_request.html', {
        'service_request_form': service_request_form,
        'patient_record': patient_record,
    })
    



#GENERATE THE STATEMENT OF OUTPATIENT REPORT
@login_required(login_url="authentication:my-login") 
def outpatient_report(request):
    try:
        if request.method == 'POST':
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        age_group,
                        SUM(CASE WHEN gender = 'M' AND client_status = 'insured' AND client_type = 'New client' THEN 1 ELSE 0 END) AS New_Male_Insured,
                        SUM(CASE WHEN gender = 'M' AND client_status = 'insured' AND client_type = 'old client' THEN 1 ELSE 0 END) AS Old_Male_Insured,
                        SUM(CASE WHEN gender = 'M' AND client_status = 'non-insured' AND client_type = 'New client' THEN 1 ELSE 0 END) AS New_Male_Non_Insured,
                        SUM(CASE WHEN gender = 'M' AND client_status = 'non-insured' AND client_type = 'old client' THEN 1 ELSE 0 END) AS Old_Male_Non_Insured,
                        SUM(CASE WHEN gender = 'F' AND client_status = 'insured' AND client_type = 'New client' THEN 1 ELSE 0 END) AS New_Female_Insured,
                        SUM(CASE WHEN gender = 'F' AND client_status = 'insured' AND client_type = 'old client' THEN 1 ELSE 0 END) AS Old_Female_Insured,
                        SUM(CASE WHEN gender = 'F' AND client_status = 'non-insured' AND client_type = 'New client' THEN 1 ELSE 0 END) AS New_Female_Non_Insured,
                        SUM(CASE WHEN gender = 'F' AND client_status = 'non-insured' AND client_type = 'old client' THEN 1 ELSE 0 END) AS Old_Female_Non_Insured
                    FROM patient_records_patientrecord
                    WHERE date_of_visit BETWEEN %s AND %s
                    GROUP BY age_group
                """, [start_date, end_date])
                rows = cursor.fetchall()
        else:
            rows = None
    except OperationalError as e:
        # Handle the operational error (e.g., database connection issue)
        print(f"Operational error: {e}")
        rows = None

    return render(request, 'patient_records/outpatient_report.html', {'rows': rows})
