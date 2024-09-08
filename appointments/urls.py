from django.urls import path
from . import views

urlpatterns = [
    path('api/appointments/', views.appointment_list, name='appointment_list'),
    path('api/appointments/create/', views.create_appointment, name='create_appointment'),
     path('create/', views.create_appointment, name='create_appointment'),
]
