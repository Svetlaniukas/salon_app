from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ClientForm
from .models import Client
from appointments.models import Appointment  # Используем модель из приложения appointments


# Главная страница
def home(request):
    return render(request, 'home.html')


# Регистрация клиента
def register_client(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user)
            login(request, user)
            return redirect('client_profile')  # Перенаправление на профиль клиента
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



# Страница создания профиля клиента
@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('client_dashboard')  # Перенаправляем на панель клиента
    else:
        form = ClientForm()
    
    return render(request, 'clients/profile_create.html', {'form': form})


# Панель клиента
@login_required
def client_dashboard(request):
    try:
        client = request.user.client
    except Client.DoesNotExist:
        return redirect('profile_create')  # Если нет профиля, перенаправляем на создание профиля
    return render(request, 'clients/client_dashboard.html', {'client': client})


# Профиль клиента
@login_required
def client_profile(request):
    client = request.user.client
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)  # Добавляем request.FILES
        if form.is_valid():
            form.save()
            return redirect('client_profile')  # Перенаправляем на ту же страницу после сохранения
    else:
        form = ClientForm(instance=client)

    return render(request, 'clients/profile.html', {'client': client, 'form': form})


def custom_login_redirect(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'client'):
            return redirect('client_profile')  # Профиль клиента
        elif hasattr(request.user, 'hairdresser'):
            return redirect('hairdresser_profile')  # Профиль парикмахера
    return redirect('home')