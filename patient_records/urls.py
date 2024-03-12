from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views
from .views import download_data

urlpatterns = [
    path('download/<str:format>/', download_data, name='download_data'), #download data url
    path('<int:id>', views.view_patient, name='view-patient'),
    path('view_all_patients', views.view_all_patients, name='view_all_patients'),
    path('add/', views.add, name='add'),
    path('<int:id>/', views.view_patient, name='view_patient'),
    path('patient-records/edit/<int:id>/', views.edit, name='edit'),
    path('<int:id>/delete/', views.delete, name='delete'),
    # path('view-all-patients-modal/', views.view_all_patients, name='view_all_patients_modal'),
    # Authentication URLs ------------------------------------------------
    path('', views.index, name="patient-records"),  # Adjusted URL pattern
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
