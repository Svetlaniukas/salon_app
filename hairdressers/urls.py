from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_hairdresser, name='register_hairdresser'),
    path('profile/', views.hairdresser_profile, name='hairdresser_profile'),
    path('dashboard/', views.hairdresser_dashboard, name='hairdresser_dashboard'),
    path('profile/create/', views.hairdresser_profile_create, name='hairdresser_profile_create'),  # Теперь это представление существует
    path('api/hairdresser_appointments/', views.hairdresser_appointments, name='hairdresser_appointments'),
    path('api/list/', views.hairdresser_list, name='hairdresser_list'),  # Новый маршрут для списка парикмахеров
]
