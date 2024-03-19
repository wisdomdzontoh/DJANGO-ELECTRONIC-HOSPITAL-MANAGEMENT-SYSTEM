from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
#from .forms import NurseStationForm
from nursestation.models import NurseStation




#View index page
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'consultingroom/index.html')


#VIEW MY APPOINTMENTS
@login_required(login_url="authentication:my-login")
def view_my_appointments(request):
    nursestations = NurseStation.objects.filter(doctor=request.user).order_by('-date_of_appointment')
    return render(request, 'consultingroom/view-my-appointments.html', {'nursestations': nursestations})


#VIEW AND ADD DIAGNOSIS
@login_required(login_url="authentication:my-login") 
def add_diagnosis(request, id):
    appointment = NurseStation.objects.get(pk=id)
    patient_record = appointment.patient  # Assuming patient_id is the ForeignKey to PatientRecord

    return render(request, 'consultingroom/consultingroom-register.html', {
        'appointment': appointment,
        'patient_record': patient_record,  # Pass the patient_record to the template
    })
