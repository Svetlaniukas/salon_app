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
from clients import views as client_views  # Импортируем представления из приложения clients

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),  # Добавляем маршруты для приложения clients
    path('hairdressers/', include('hairdressers.urls')),  # Маршруты для парикмахеров
    path('appointments/', include('appointments.urls')),  # Маршруты для записей
    path('register/', client_views.register, name='register'),  # Регистрация
    path('accounts/', include('django.contrib.auth.urls')),  # Стандартные маршруты для авторизации
    path('', client_views.home, name='home'),  # Главная страница
]
