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


@login_required(login_url="authentication:my-login")
def view_all_patients(request):
    patient_records = PatientRecord.objects.all()
    paginator = Paginator(patient_records, 10)
    page_number = request.GET.get('page')
    patient_records = paginator.get_page(page_number)
    return render(request, 'patient_records/view_all_patients.html', {'patient_records': patient_records})

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
            return redirect('view_all_patients')
    else:
        form = PatientRecordForm()
    return render(request, 'patient_records/add.html', {'form': form})

#edit function to edit and update
@login_required(login_url="authentication:my-login") 
def edit(request, id):
    patient_record = PatientRecord.objects.get(pk=id)
    if request.method == 'POST':
        form = PatientRecordForm(request.POST, instance=patient_record)
        if form.is_valid():
            # Set the last_updated field to the current date and time
            patient_record.last_updated = timezone.now()
            form.save()
            return redirect('view_all_patients')
    else:
        form = PatientRecordForm(instance=patient_record)
    return render(request, 'patient_records/edit.html', {'form': form})


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