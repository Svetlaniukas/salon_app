from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_hairdresser, name='register_hairdresser'),
    path('dashboard/', views.hairdresser_dashboard, name='hairdresser_dashboard'),
    path('login/', views.login, name='login'),
]
