from django.urls import path
from . import views
from clients import views as client_views  # Импорт представления для клиента

urlpatterns = [
    path('register/', views.register_client, name='register_client'),
    path('profile/', views.client_profile, name='client_profile'),
    path('dashboard/', views.client_dashboard, name='client_dashboard'),
    path('profile/create/', views.profile_create, name='profile_create'),  # Создание профиля
    path('login-redirect/', client_views.custom_login_redirect, name='custom_login_redirect'),  # Добавьте этот маршрут
]
