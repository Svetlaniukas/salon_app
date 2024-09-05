from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_appointment, name='create_appointment'),
    path('edit/<int:pk>/', views.edit_appointment, name='edit_appointment'),
]
