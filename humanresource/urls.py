from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views


urlpatterns = [
    path('staffs/edit/<int:id>/', views.edit_staff, name='edit-staff'),
    path('staffs/<int:id>/delete/', views.delete_staff, name='staff-delete'),
    path('add-staff/', views.add_staff, name='add-staff'),
    path('view-all-staff/', views.view_all_staff, name='view-all-staff'),
    path('', views.index, name="humanresource"),  # Added URL pattern for index view
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
