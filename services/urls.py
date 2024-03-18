from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views


urlpatterns = [
    path('<int:id>/', views.view_service, name='view-service'),
    path('services/edit/<int:id>/', views.edit, name='edit-service'),
    path('services/<int:id>/delete/', views.delete_service, name='services/delete'),
    path('add/', views.add_service, name='add-service'),
    path('view-all/', views.view_all_services, name='view-all'),
    path('', views.index, name="services"),  # Added URL pattern for index view
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
