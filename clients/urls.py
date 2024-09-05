from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.client_dashboard, name='client_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.profile_create, name='profile_create'),  # Маршрут для создания профиля
]
