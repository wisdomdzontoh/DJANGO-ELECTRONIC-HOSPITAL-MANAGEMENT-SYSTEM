from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Department
from .forms import DepartmentForm
from django.utils import timezone
from django.http import Http404

# View index page
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'departments/index.html')

# View all departments
@login_required(login_url="authentication:my-login")
def view_all_departments(request):
    # Retrieve department records sorted by last_updated
    departments = Department.objects.order_by('-last_updated').all()
    return render(request, 'departments/view-all.html', {'departments': departments})

# Add a department
@login_required(login_url="authentication:my-login")
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.instance.last_updated = timezone.now()  # SET THE LAST UPDATED TIME TO THE CURRENT TIME ZONE
            form.save()
            return render(request, 'departments/success.html')  # Corrected redirect call
            
    else:
        form = DepartmentForm()
    return render(request, 'departments/add.html', {'form': form})


# edit department
@login_required(login_url="authentication:my-login") 
def edit(request, id):
    department = get_object_or_404(Department, pk=id)
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            return render(request, 'departments/success.html')
            
    else:
        form = DepartmentForm(instance=department)
        
    return render(request, 'departments/edit.html', {
        'form': form,
        'department': department,
    })



#delete patient records
@login_required(login_url="authentication:my-login") 
def delete_department(request, id):
    if request.method == 'POST':
        department = Department.objects.get(pk=id)
        department.delete()
    return redirect('view-all')

