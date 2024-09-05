from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm  # Импортируем форму регистрации
from django.contrib.auth.decorators import login_required  # Добавляем импорт login_required


def register_hairdresser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически логиним пользователя после регистрации
            return redirect('hairdresser_dashboard')  # Перенаправляем на панель парикмахера
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def hairdresser_dashboard(request):
    hairdresser = request.user.hairdresser
    appointments = hairdresser.appointments_as_hairdresser.all()
    return render(request, 'hairdressers/hairdresser_dashboard.html', {'appointments': appointments})

@login_required
def appointment_list(request):
    hairdresser = request.user.hairdresser
    appointments = hairdresser.appointments_as_hairdresser.all()
    return render(request, 'hairdressers/appointment_list.html', {'appointments': appointments})
