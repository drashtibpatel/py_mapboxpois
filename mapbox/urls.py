from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_mapbox, name='view mapbox')
]