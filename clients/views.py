from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ClientForm
from .models import Client

# Представление для регистрации
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Создаем объект Client для нового пользователя
            Client.objects.create(user=user)
            login(request, user)  # Логиним пользователя после регистрации
            return redirect('client_dashboard')  # Перенаправляем на панель клиента
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# Главная страница
def home(request):
    return render(request, 'home.html')

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

# Панель клиента
@login_required
def client_dashboard(request):
    try:
        client = request.user.client  # Пытаемся получить объект Client для текущего пользователя
    except Client.DoesNotExist:
        # Если объект Client не существует, перенаправляем пользователя на страницу создания профиля
        return redirect('profile_create')  # Ты можешь перенаправить на нужную страницу или создать новый объект

    # Логика для панели управления клиента
    return render(request, 'clients/client_dashboard.html', {'client': client})

# Профиль клиента
@login_required
def profile(request):
    client = request.user.client
    return render(request, 'clients/profile.html', {'client': client})
