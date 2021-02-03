from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_pois, name='add_pois'),
    path('add/', views.add_pois, name='add_pois'),
    path('view/', views.view_pois, name='view_pois'),
    path('edit/<int:id>', views.edit_pois, name='edit_pois'), 
    path('delete/<int:id>', views.delete_pois, name='delete_pois'),
]