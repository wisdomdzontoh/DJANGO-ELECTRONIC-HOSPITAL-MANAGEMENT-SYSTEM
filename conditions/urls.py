from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views


urlpatterns = [
    path('conditions/edit/<int:id>/', views.edit, name='edit-conditions'),
    path('conditions/<int:id>/delete/', views.delete_condition, name='conditions/delete'),
    path('add/', views.add_condition, name='add-condition'),
    path('view-all/', views.view_all_conditions, name='view-all-conditions'),
    path('', views.index, name="conditions"),  # Added URL pattern for index view
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
