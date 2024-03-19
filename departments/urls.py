from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views


urlpatterns = [
    path('departments/edit/<int:id>/', views.edit, name='edit-department'),
    path('departments/<int:id>/delete/', views.delete_department, name='departments/delete'),
    path('add/', views.add_department, name='add-department'),
    path('view-all/', views.view_all_departments, name='view-all'),
    path('', views.index, name="departments"),  # Added URL pattern for index view
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
