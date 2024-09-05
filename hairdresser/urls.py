"""
URL configuration for hairdresser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from clients import views as client_views
from hairdressers import views as hairdresser_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # Для маршрутов восстановления пароля

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),  # Маршруты для клиентов
    path('hairdressers/', include('hairdressers.urls')),  # Маршруты для парикмахеров
    path('appointments/', include('appointments.urls')),  # Маршруты для записей
    path('register/', client_views.register_client, name='register'),  # Регистрация клиента
    path('register_hairdresser/', hairdresser_views.register_hairdresser, name='register_hairdresser'),  # Регистрация парикмахера
    path('accounts/', include('django.contrib.auth.urls')),  # Стандартные маршруты для авторизации

    # Главная страница
    path('', client_views.home, name='home'),
    path('login-redirect/', client_views.custom_login_redirect, name='custom_login_redirect'),  # Добавьте этот маршрут

    # Маршруты для восстановления пароля
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Маршруты для профилей
    path('client/profile/', client_views.client_profile, name='client_profile'),  # Профиль клиента
    path('hairdresser/profile/', hairdresser_views.hairdresser_profile, name='hairdresser_profile'),  # Профиль парикмахера
]

# Обработка медиафайлов в режиме отладки (development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
