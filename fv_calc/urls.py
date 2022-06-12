from django.urls import path
from . import views

urlpatterns = [
  path('add-data/', views.addData, name='add_data'),
  path('view-data/<int:pk>/', views.viewData, name='view_data'),
  path('delete-data/<int:pk>/', views.deleteData, name='delete_data'),
  path('edit-data/<int:pk>/', views.editData, name='edit_data'),
]