from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Conditions
from .forms import ConditionsForm
from django.utils import timezone
from django.http import Http404

# View index page
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'conditions/index.html')

# View all departments
@login_required(login_url="authentication:my-login")
def view_all_conditions(request):
    # Retrieve department records sorted by last_updated
    conditions = Conditions.objects.order_by('-last_updated').all()
    return render(request, 'conditions/view-all.html', {'conditions': conditions})

# Add a department
@login_required(login_url="authentication:my-login")
def add_condition(request):
    if request.method == 'POST':
        form = ConditionsForm(request.POST)
        if form.is_valid():
            form.instance.last_updated = timezone.now()  # SET THE LAST UPDATED TIME TO THE CURRENT TIME ZONE
            form.save()
            return render(request, 'conditions/success.html')  # Corrected redirect call
            
    else:
        form = ConditionsForm()
    return render(request, 'conditions/add.html', {'form': form})


# edit department
@login_required(login_url="authentication:my-login") 
def edit(request, id):
    conditions = get_object_or_404(Conditions, pk=id)
    
    if request.method == 'POST':
        form = ConditionsForm(request.POST, instance=conditions)

        if form.is_valid():
            form.save()
            return render(request, 'conditions/update-success.html')
            
    else:
        form = ConditionsForm(instance=conditions)
        
    return render(request, 'conditions/edit.html', {
        'form': form,
        'conditions': conditions,
    })



#delete patient records
@login_required(login_url="authentication:my-login") 
def delete_condition(request, id):
    if request.method == 'POST':
        conditions = Conditions.objects.get(pk=id)
        conditions.delete()
    return redirect('view-all-conditions')