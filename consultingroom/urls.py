from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views



urlpatterns = [
    #path('book/', views.book_appointment, name='book'),
    #path('confirmation/', views.appointment_confirmation, name='confirmation'),
    path('<int:patient_id>/', views.add_diagnosis, name='add-diagnosis'),
    path('view-my-appointments/', views.view_my_appointments, name='view-my-appointments'),
    path('', views.index, name="consultingroom"),  # Added URL pattern for index view
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
