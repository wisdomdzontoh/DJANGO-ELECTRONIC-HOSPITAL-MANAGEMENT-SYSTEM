from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views


urlpatterns = [
    path('laboratory/edit/<int:id>/', views.edit, name='edit-test-type'),
    path('laboratory/<int:id>/delete-test-type/', views.delete_test_type, name='laboratory/delete-test-type'),
    path('add-test-type/', views.add_test_type, name='add-test-type'),
    path('view-all-tests/', views.view_all_tests, name='view-all-tests'),
    path('', views.index, name="laboratory"),  # Added URL pattern for index view
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
