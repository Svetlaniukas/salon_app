from django.contrib import admin
from django.urls import path, include
from clients import views as client_views
from . import views 
from clients import views as client_views  # Импорт представления для клиента


urlpatterns = [

    path('', client_views.home, name='home'),  # Главная страница
    path('clients/', include('clients.urls')),  # Добавляем маршруты для клиентов
    path('profile/create/', views.hairdresser_profile_create, name='hairdresser_profile_create'),  # Создание профиля парикмахера
    path('register/', views.register_hairdresser, name='register_hairdresser'),
    path('profile/', views.hairdresser_profile, name='hairdresser_profile'),
    path('dashboard/', views.hairdresser_dashboard, name='hairdresser_dashboard'),
    path('login-redirect/', client_views.custom_login_redirect, name='custom_login_redirect'),  # Добавьте этот маршрут
]

