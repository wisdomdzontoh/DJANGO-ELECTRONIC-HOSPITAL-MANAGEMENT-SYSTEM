from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .forms import NurseStationForm
#from .models import NurseStation



#View index page
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'consultingroom/index.html')