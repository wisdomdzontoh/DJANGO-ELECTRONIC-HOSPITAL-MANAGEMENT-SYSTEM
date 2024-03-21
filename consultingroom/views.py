from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
#from .forms import NurseStationForm
from nursestation.models import NurseStation
from consultingroom.models import LabTest, ConsultingRoom
from consultingroom.forms import LabTestForm, ConsultingRoomForm
from patient_records.models import PatientRecord




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
def add_diagnosis(request, patient_id):
    patient_record = NurseStation.objects.get(pk=patient_id)
    lab_tests = LabTest.objects.filter(lab_patient__patient=patient_record)

    if request.method == 'POST':
        diagnosis_form = ConsultingRoomForm(request.POST)
        lab_test_form = LabTestForm(request.POST)
        if diagnosis_form.is_valid():
            diagnosis_form.save()
            return redirect('add_diagnosis', patient_id=patient_id)
        if lab_test_form.is_valid():
            lab_test_form.save()
            return redirect('add_diagnosis', patient_id=patient_id)
    else:
        diagnosis_form = ConsultingRoomForm()
        lab_test_form = LabTestForm()

    context = {
        'patient_record': patient_record,
        'lab_tests': lab_tests,
        'diagnosis_form': diagnosis_form,
        'lab_test_form': lab_test_form,
    }
    return render(request, 'consultingroom/consultingroom-register.html', context)

def add_lab_test(request, consulting_room_id):
    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            lab_test = form.save(commit=False)
            lab_test.lab_patient_id = consulting_room_id
            lab_test.save()
            return redirect('add-diagnosis', patient_id=consulting_room_id)
    else:
        form = LabTestForm()
    return render(request, 'consultingroom/consultingroom-register.html', {'form': form})
