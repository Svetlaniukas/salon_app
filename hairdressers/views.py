from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, HairdresserForm
from .models import Hairdresser
from appointments.models import Appointment
from django.http import JsonResponse
from django.contrib.auth.models import User

# Главная страница
def home(request):
    context = {}
    if request.user.is_authenticated:
        context['is_client'] = hasattr(request.user, 'client_profile')
        context['is_hairdresser'] = hasattr(request.user, 'hairdresser_profile')
    return render(request, 'home.html', context)

# Регистрация парикмахера
# Регистрация парикмахера
def register_hairdresser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Создаем нового пользователя
            # Создаем профиль парикмахера для этого пользователя
            Hairdresser.objects.create(
                user=user,
                name=user.username,  # Используем имя пользователя по умолчанию для поля name
                email=user.email,  # Используем email пользователя
                specialization='General Hairdresser',  # Дефолтная специализация
                experience=0,  # Опыт по умолчанию
                availability='9 AM - 6 PM'  # Доступность по умолчанию
            )
            login(request, user)  # Авторизуем нового пользователя
            return redirect('hairdresser_dashboard')  # Перенаправляем на дашборд парикмахера
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



# Страница создания профиля парикмахера
@login_required
def hairdresser_profile_create(request):
    if request.method == 'POST':
        form = HairdresserForm(request.POST)
        if form.is_valid():
            hairdresser = form.save(commit=False)
            hairdresser.user = request.user
            hairdresser.save()
            return redirect('hairdresser_dashboard')
    else:
        form = HairdresserForm()
    return render(request, 'hairdressers/profile_create.html', {'form': form})

# API для записей парикмахера
@login_required
def hairdresser_appointments(request):
    hairdresser = request.user.hairdresser_profile
    appointments = Appointment.objects.filter(hairdresser=hairdresser)

    events = []
    for appointment in appointments:
        events.append({
            'id': appointment.id,
            'title': f'{appointment.service} - {appointment.client.user.username}',  # Отображаем имя клиента
            'start': f'{appointment.date}T{appointment.start_time}',
            'end': f'{appointment.date}T{appointment.end_time}',
            'client': appointment.client.user.username,  # Имя клиента
            'service': appointment.service
        })

    return JsonResponse(events, safe=False)


# Панель парикмахера
@login_required
def hairdresser_dashboard(request):
    hairdresser = request.user.hairdresser_profile
    appointments = Appointment.objects.filter(hairdresser=hairdresser)  # Записи только для текущего парикмахера
    return render(request, 'hairdressers/hairdresser_dashboard.html', {
        'hairdresser': hairdresser,
        'appointments': appointments
    })




# Профиль парикмахера
@login_required
def hairdresser_profile(request):
    hairdresser = request.user.hairdresser_profile
    if request.method == 'POST':
        form = HairdresserForm(request.POST, request.FILES, instance=hairdresser)
        if form.is_valid():
            form.save()
            return redirect('hairdresser_profile')
    else:
        form = HairdresserForm(instance=hairdresser)
    return render(request, 'hairdressers/profile.html', {'hairdresser': hairdresser, 'form': form})

# Перенаправление после входа
def custom_login_redirect(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'client_profile'):
            return redirect('client_profile')  # Перенаправляем клиента на страницу профиля
        elif hasattr(request.user, 'hairdresser_profile'):
            return redirect('hairdresser_profile')  # Перенаправляем парикмахера на страницу профиля
    return redirect('home')

# Представление для получения списка всех парикмахеров
@login_required
def hairdresser_list(request):
    hairdressers = Hairdresser.objects.all()
    hairdresser_data = [
        {
            'id': hairdresser.id,
            'name': hairdresser.user.username
        }
        for hairdresser in hairdressers
    ]
    return JsonResponse({'hairdressers': hairdresser_data})
