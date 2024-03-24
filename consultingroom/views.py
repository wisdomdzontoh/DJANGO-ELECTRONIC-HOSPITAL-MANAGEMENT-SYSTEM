from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ConsultingRoomForm, LabTestForm
from .models import LabTest
from patient_records.models import PatientRecord
from nursestation.models import NurseStation
from nursestation.forms import NurseStationForm


# VIEW INDEX PAGE
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'consultingroom/index.html')


#PATIENT PAGE TO LOGIN
def patient_page(request, patient_id):
    patient_record = get_object_or_404(PatientRecord, patient_id=patient_id)
    # Render patient page with CRUD functionalities
    return render(request, 'consultingroom/patient_page.html', {'patient_record': patient_record})


# PATIENT page to perform crud operations
def search_patient(request):
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id')
        if patient_id:
            return redirect('patient_page', patient_id=patient_id)
    return render(request, 'consultingroom/search_patient.html')



# VIEW ALL MY APPOINTMENTS
@login_required(login_url="authentication:my-login")
def view_my_appointments(request):
    nursestations = NurseStation.objects.filter(doctor=request.user).order_by('-date_of_appointment')
    return render(request, 'consultingroom/view-my-appointments.html', {'nursestations': nursestations})


# CONFIRM MY APPOINTMENT
@login_required(login_url="authentication:my-login") 
def confirm_my_appointment(request, id):
    nurse_station = get_object_or_404(NurseStation, pk=id)
    
    if request.method == 'POST':
        form = NurseStationForm(request.POST, instance=nurse_station)
        
        if form.is_valid():
            form.save()
            return render(request, 'consultingroom/update-success.html')
    else:
        form = NurseStationForm(instance=nurse_station)
    
    return render(request, 'consultingroom/confirm-appointment.html', {
        'form': form,
        'nurse_station': nurse_station,
    })






"""
@login_required(login_url="authentication:my-login")
def add_diagnosis(request, patient_id):
    patient_record = get_object_or_404(NurseStation, pk=patient_id)
    lab_tests = LabTest.objects.filter(lab_patient__patient=patient_record)
    
    diagnosis_form = ConsultingRoomForm()
    lab_test_form = LabTestForm()

    if request.method == 'POST':
        if 'diagnosis_submit' in request.POST:
            diagnosis_form = ConsultingRoomForm(request.POST)
            if diagnosis_form.is_valid():
                diagnosis = diagnosis_form.save(commit=False)
                diagnosis.patient_record = patient_record
                diagnosis.save()
                return redirect('add_diagnosis', patient_id=patient_id)
        elif 'lab_test_submit' in request.POST:
            lab_test_form = LabTestForm(request.POST)
            if lab_test_form.is_valid():
                lab_test = lab_test_form.save(commit=False)
                lab_test.lab_patient = patient_record
                lab_test.save()
                return redirect('add_diagnosis', patient_id=patient_id)

    context = {
        'patient_record': patient_record,
        'lab_tests': lab_tests,
        'diagnosis_form': diagnosis_form,
        'lab_test_form': lab_test_form,
    }
    return render(request, 'consultingroom/consultingroom-register.html', context)
"""

#ADDING A DIAGNOSIS
def add_diagnosis(request, patient_id):
    patient_record = PatientRecord.objects.get(pk=patient_id)
    appointment = NurseStation.objects.filter(patient__patient_id=patient_record)
    
    
    diagnosis_form = ConsultingRoomForm()
    lab_test_form = LabTestForm()

    if request.method == 'POST':
        if 'diagnosis_submit' in request.POST:
            diagnosis_form = ConsultingRoomForm(request.POST)
            if diagnosis_form.is_valid():
                diagnosis = diagnosis_form.save(commit=False)
                diagnosis.patient_record = patient_record
                diagnosis.save()
                return redirect('add_diagnosis', patient_id=patient_id)
        elif 'lab_test_submit' in request.POST:
            lab_test_form = LabTestForm(request.POST)
            if lab_test_form.is_valid():
                lab_test = lab_test_form.save(commit=False)
                lab_test.lab_patient = patient_record
                lab_test.save()
                return redirect('add_diagnosis', patient_id=patient_id)
    
    
    context = {
        'patient_record': patient_record,
        'appointment': appointment,
        'diagnosis_form': diagnosis_form,
        'lab_test_form': lab_test_form,
    }
    return render(request, 'consultingroom/consultingroom-register.html', context)




