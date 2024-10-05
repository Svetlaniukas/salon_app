from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ClientForm
from .models import Client
from appointments.models import Appointment
from datetime import timedelta

from django.http import JsonResponse

from hairdressers.models import Hairdresser


def home(request):
    """Render the homepage with a list of hairdressers and their ratings."""
    hairdressers = Hairdresser.objects.all()
    for hairdresser in hairdressers:
        avg_rating = hairdresser.get_average_rating()
        hairdresser.filled_stars = int(avg_rating)  # Filled stars based on average rating
        hairdresser.empty_stars = 5 - int(avg_rating)  # Empty stars

    context = {
        'hairdressers': hairdressers,
        'is_client': hasattr(request.user, 'client_profile') if request.user.is_authenticated else False,
        'is_hairdresser': hasattr(request.user, 'hairdresser_profile') if request.user.is_authenticated else False,
    }
    return render(request, 'home.html', context)


# Client registration
def register_client(request):
    """Handle client registration form submission and profile creation."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user)  # Create client profile after registration
            login(request, user)
            return redirect('client_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Client profile creation page
@login_required
def profile_create(request):
    """Allows a logged-in client to create their profile."""
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

# API for client appointments
@login_required
def client_appointments(request):
    """Returns a list of client appointments in JSON format."""
    client = request.user.client_profile  # Get the logged-in client's profile
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

# Client dashboard
@login_required
def client_dashboard(request):
    """Renders the client's dashboard with a list of their appointments."""
    client = request.user.client_profile
    appointments = Appointment.objects.filter(client=client)
    return render(request, 'clients/client_dashboard.html', {
        'client': client,
        'appointments': appointments
    })

# Client profile page
@login_required
def client_profile(request):
    """Renders the client's profile page and allows profile updates."""
    client = request.user.client_profile
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_profile')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/profile.html', {'client': client, 'form': form})

# Custom login redirect
def custom_login_redirect(request):
    """Redirects the user to the appropriate profile page based on their role."""
    if request.user.is_authenticated:
        if hasattr(request.user, 'client_profile'):
            return redirect('client_profile')  # Redirect client to their profile page
        elif hasattr(request.user, 'hairdresser_profile'):
            return redirect('hairdresser_profile')  # Redirect hairdresser to their profile page
    return redirect('home')  # Redirect to home if no user is authenticated
