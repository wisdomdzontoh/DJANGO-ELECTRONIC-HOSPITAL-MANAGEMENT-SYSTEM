from django.urls import path
from authentication import views as auth_views
from . import views

urlpatterns = [
    #path('patient/<str:patient_id>/', views.patient_view_profile, name='patient-view-profile'),
    path('search_patient/', views.search_patient, name='search_patient'),
    path('patient/<str:patient_id>/', views.patient_page, name='patient_page'),

    path('confirm-appointment/<int:id>/', views.confirm_my_appointment, name='confirm-appointment'),
    path('<int:patient_id>/', views.add_diagnosis, name='add-diagnosis'),
    path('view-my-appointments/', views.view_my_appointments, name='view-my-appointments'),
    path('', views.index, name="consultingroom"),
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),
]
