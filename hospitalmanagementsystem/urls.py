
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),  # authentication urls for login and signup pages
    path('patient-records/', include('patient_records.urls')),
    
    
    path('admin_tools_stats/', include('admin_tools_stats.urls')), #for django-admin chart view
    
    
    
    path("__reload__/", include("django_browser_reload.urls")),
]
