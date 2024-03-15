from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HumanResource
from .forms import HumanResourceForm
from django.utils import timezone
from django.http import Http404

# View index page
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'humanresource/index.html')


# View all departments
@login_required(login_url="authentication:my-login")
def view_all_staff(request):
    # Retrieve department records sorted by last_updated
    staffs = HumanResource.objects.order_by('-last_updated').all()
    return render(request, 'humanresource/view-all-staff.html', {'staffs': staffs})



# add a new staff
@login_required(login_url="authentication:my-login")
def add_staff(request):
    if request.method == 'POST':
        form = HumanResourceForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return render(request, 'humanresource/success.html')
    else:
        form = HumanResourceForm()
    return render(request, 'humanresource/add.html', {'form': form})



#EDIT STAFF HERE
@login_required(login_url='authentication:my-login')
def edit_staff(request, id):
    staff = get_object_or_404(HumanResource, pk=id)
    
    if  request.method=='POST':
        form = HumanResourceForm(request.POST, instance=staff)
        
        if form.is_valid():
            form.save()
            return render(request, 'humanresource/update-success.html')
        
    else:
        form = HumanResourceForm(instance=staff)
        
    return render(request, 'humanresource/edit.html', {
        'form': form,
        'staff': staff,
    })
        

#delete staff records
@login_required(login_url="authentication:my-login") 
def delete_staff(request, id):
    if request.method == 'POST':
        staff = HumanResource.objects.get(pk=id)
        staff.delete()
    return redirect('view-all-staff')