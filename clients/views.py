from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ClientForm
from .models import Client
from appointments.models import Appointment
from datetime import timedelta

from django.http import JsonResponse

# Главная страница
from django.shortcuts import render

def home(request):
    context = {}
    if request.user.is_authenticated:
        context['is_client'] = hasattr(request.user, 'client_profile')
        context['is_hairdresser'] = hasattr(request.user, 'hairdresser_profile')
    return render(request, 'home.html', context)

# Регистрация клиента
def register_client(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user)  # Создаём профиль клиента после регистрации
            login(request, user)
            return redirect('client_dashboard')
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
            return redirect('client_dashboard')
    else:
        form = ClientForm()
    return render(request, 'clients/profile_create.html', {'form': form})

# API для записей клиента
# API для записей клиента
@login_required
def client_appointments(request):
    client = request.user.client_profile  # Получаем профиль клиента
    appointments = Appointment.objects.filter(client=client)
    
    events = []
    for appointment in appointments:
        events.append({
            'id': appointment.id,
            'title': f'{appointment.service} with {appointment.hairdresser.user.username}',
            'start': f'{appointment.date}T{appointment.start_time}',
            'end': f'{appointment.date}T{appointment.end_time}',
        })

    return JsonResponse(events, safe=False)

# Панель клиента
@login_required
def client_dashboard(request):
    client = request.user.client_profile
    appointments = Appointment.objects.filter(client=client)
    return render(request, 'clients/client_dashboard.html', {
        'client': client,
        'appointments': appointments
    })

# Профиль клиента
@login_required
def client_profile(request):
    client = request.user.client_profile
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_profile')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/profile.html', {'client': client, 'form': form})

# Перенаправление после входа
def custom_login_redirect(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'client_profile'):
            return redirect('client_profile')  # Перенаправляем клиента на страницу профиля
        elif hasattr(request.user, 'hairdresser_profile'):
            return redirect('hairdresser_profile')  # Перенаправляем парикмахера на страницу профиля
    return redirect('home')  # Если никто не вошел в систему, перенаправляем на главную

