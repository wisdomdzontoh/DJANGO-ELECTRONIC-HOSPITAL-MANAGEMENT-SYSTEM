from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TestTypes
from .forms import TestTypesForm
from django.utils import timezone
from django.http import Http404


# Create your views here.
# View index page
@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'laboratory/index.html')

# View all departments
@login_required(login_url="authentication:my-login")
def view_all_tests(request):
    # Retrieve test_types records sorted by last_updated
    test_types = TestTypes.objects.order_by('-last_updated').all()
    return render(request, 'laboratory/view-all-test-types.html', {'test_types': test_types})

# Add a test-type
@login_required(login_url='authentication:my-login')
def add_test_type(request):
    if request.method == "POST":
        form = TestTypesForm(request.POST)
        if form.is_valid():
            form.instance.last_updated = timezone.now()
            form.save()
            return render (request, 'laboratory/success.html')
        
    else:
        form = TestTypesForm()
    return render(request, 'laboratory/add-test-type.html', {'form': form})


# edit department
@login_required(login_url="authentication:my-login") 
def edit(request, id):
    test_types = get_object_or_404(TestTypes, pk=id)
    
    if request.method == 'POST':
        form = TestTypesForm(request.POST, instance=test_types)

        if form.is_valid():
            form.save()
            return render(request, 'laboratory/update-success.html')
            
    else:
        form = TestTypesForm(instance=test_types)
        
    return render(request, 'laboratory/edit.html', {
        'form': form,
        'test_types': test_types,
    })



#delete patient records
@login_required(login_url="authentication:my-login") 
def delete_test_type(request, id):
    if request.method == 'POST':
        test_types = TestTypes.objects.get(pk=id)
        test_types.delete()
    return redirect('view-all-tests')