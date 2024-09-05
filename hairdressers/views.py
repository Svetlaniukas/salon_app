from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, HairdresserForm
from .models import Hairdresser
from django.contrib.auth.decorators import login_required

# Главная страница
def home(request):
    return render(request, 'home.html')


# Регистрация парикмахера
def register_hairdresser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Hairdresser.objects.create(user=user)
            login(request, user)
            return redirect('hairdresser_profile')  # Перенаправление на профиль парикмахера
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def hairdresser_profile(request):
    hairdresser = request.user.hairdresser  # Получаем текущего парикмахера
    if request.method == 'POST':
        form = HairdresserForm(request.POST, request.FILES, instance=hairdresser)  # Передаем request.FILES для обработки загружаемых файлов
        if form.is_valid():
            form.save()  # Сохраняем форму
            return redirect('hairdresser_profile')  # Перенаправляем на ту же страницу после сохранения
    else:
        form = HairdresserForm(instance=hairdresser)  # Заполняем форму данными текущего парикмахера

    return render(request, 'hairdressers/profile.html', {'form': form, 'hairdresser': hairdresser})


# Страница создания профиля парикмахера
@login_required
def hairdresser_profile_create(request):
    if request.method == 'POST':
        form = HairdresserForm(request.POST)
        if form.is_valid():
            hairdresser = form.save(commit=False)
            hairdresser.user = request.user
            hairdresser.save()
            return redirect('hairdresser_dashboard')  # Перенаправляем на панель парикмахера
    else:
        form = HairdresserForm()
    
    return render(request, 'hairdressers/profile_create.html', {'form': form})


# Панель парикмахера
@login_required
def hairdresser_dashboard(request):
    try:
        hairdresser = request.user.hairdresser
    except Hairdresser.DoesNotExist:
        return redirect('hairdresser_profile_create')
    return render(request, 'hairdressers/hairdresser_dashboard.html', {'hairdresser': hairdresser})

def custom_login_redirect(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'client'):
            return redirect('client_profile')
        elif hasattr(request.user, 'hairdresser'):
            return redirect('hairdresser_profile')
    return redirect('home')