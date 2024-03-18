from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Services
from .forms import ServicesForm
from django.utils import timezone
from django.http import Http404

# View index page
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'services/index.html')

# View all services
@login_required(login_url="authentication:my-login")
def view_all_services(request):
    # Retrieve department records sorted by last_updated
    services = Services.objects.order_by('-last_updated').all()
    return render(request, 'services/view-all.html', {'services': services})

# VIEW A SERVICE PROFILE
@login_required(login_url="authentication:my-login") 
def view_service(request, id):
    service = Services.objects.get(pk=id)
    return render(request, 'services/view.html', {'service': service})


# Add a service
@login_required(login_url="authentication:my-login")
def add_service(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.instance.last_updated = timezone.now()  # SET THE LAST UPDATED TIME TO THE CURRENT TIME ZONE
            form.save()
            return render(request, 'services/success.html')  # Corrected redirect call
            
    else:
        form = ServicesForm()
    return render(request, 'services/add.html', {'form': form})


# edit service
@login_required(login_url="authentication:my-login") 
def edit(request, id):
    service = get_object_or_404(Services, pk=id)
    
    if request.method == 'POST':
        form = ServicesForm(request.POST, instance=service)

        if form.is_valid():
            form.save()
            return render(request, 'services/update-success.html')
            
    else:
        form = ServicesForm(instance=service)
        
    return render(request, 'services/edit.html', {
        'form': form,
        'service': service,
    })



#delete service records
@login_required(login_url="authentication:my-login") 
def delete_service(request, id):
    if request.method == 'POST':
        service = Services.objects.get(pk=id)
        service.delete()
    return redirect('view-all')

