from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_client, name='register_client'),
    path('profile/', views.client_profile, name='client_profile'),
    path('dashboard/', views.client_dashboard, name='client_dashboard'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('api/client_appointments/', views.client_appointments, name='client_appointments'),
]
