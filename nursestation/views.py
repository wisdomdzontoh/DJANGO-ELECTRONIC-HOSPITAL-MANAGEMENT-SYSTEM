from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NurseStationForm
from .models import NurseStation



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
    nursestations = NurseStation.objects.filter(doctor=request.user).order_by('-date_of_appointment')
    return render(request, 'nursestation/view_appointments.html', {'nursestations': nursestations})