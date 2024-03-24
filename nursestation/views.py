from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NurseStationForm
from .models import NurseStation
from patient_records.models import PatientRecord



#View index page
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'nursestation/index.html')


#Book an appointment for the client
@login_required(login_url="authentication:my-login")
def book_appointment(request):
    if request.method == 'POST':
        form = NurseStationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'nursestation/success.html')  # Redirect to a confirmation page
    else:
        form = NurseStationForm()
    return render(request, 'nursestation/book_appointment.html', {'form': form})


# Confirmed appointments bookings 
@login_required(login_url="authentication:my-login")
def appointment_confirmation(request):
    return render(request, 'nursestation/appointment_confirmation.html')


#VIEW ALL APPOINTMENTS
@login_required(login_url="authentication:my-login")
def view_appointments(request):
    patient_records = PatientRecord.objects.all()
    nursestations = NurseStation.objects.order_by('-date_of_appointment').all()
    return render(request, 'nursestation/view_appointments.html', {'nursestations': nursestations, 'patient_records': patient_records})




# EDIT APPOINTMENT BOOKING
@login_required(login_url="authentication:my-login") 
def edit(request, id):
    nurse_station = get_object_or_404(NurseStation, pk=id)
    
    if request.method == 'POST':
        form = NurseStationForm(request.POST, instance=nurse_station)
        
        if form.is_valid():
            form.save()
            return render(request, 'nursestation/update-success.html')
    else:
        form = NurseStationForm(instance=nurse_station)
    
    return render(request, 'nursestation/edit-booking.html', {
        'form': form,
        'nurse_station': nurse_station,
    })