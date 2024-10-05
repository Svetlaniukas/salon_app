from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, HairdresserForm
from .models import Hairdresser
from appointments.models import Appointment
from django.http import JsonResponse
from .forms import RatingFilterForm
from .services import get_random_quote  # Function to get a random quote
from reviews.models import Review
from django.db.models import Avg


def home(request):
    context = {}

    # Check if the user is a client or hairdresser
    if request.user.is_authenticated:
        context['is_client'] = hasattr(request.user, 'client_profile')
        context['is_hairdresser'] = hasattr(request.user, 'hairdresser_profile')

    # Get all hairdressers
    hairdressers = Hairdresser.objects.all()

    # Filtering by rating
    if request.method == 'GET':
        form = RatingFilterForm(request.GET)
        if form.is_valid():
            min_rating = form.cleaned_data.get('min_rating')
            if min_rating:
                hairdressers = hairdressers.filter(reviews__rating__gte=min_rating).distinct()

    else:
        form = RatingFilterForm()

    # Pass the form and hairdressers to the context
    context['form'] = form
    context['hairdressers'] = hairdressers

    # Get a random quote via API
    quote_data = get_random_quote()
    context['quote'] = quote_data

    return render(request, 'home.html', context)


# Hairdresser registration
def register_hairdresser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create a new user
            # Create a hairdresser profile for this user
            Hairdresser.objects.create(
                user=user,
                name=user.username,  # Use the username as the default for the name field
                email=user.email,  # Use the user's email
                specialization='General Hairdresser',  # Default specialization
                experience=0,  # Default experience
                availability='9 AM - 6 PM'  # Default availability
            )
            login(request, user)  # Log in the new user
            return redirect('hairdresser_dashboard')  # Redirect to the hairdresser dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



# Hairdresser profile creation page
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

# API for hairdresser appointments
@login_required
def hairdresser_appointments(request):
    hairdresser = request.user.hairdresser_profile
    appointments = Appointment.objects.filter(hairdresser=hairdresser)

    events = []
    for appointment in appointments:
        events.append({
            'id': appointment.id,
            'title': f'{appointment.service} - {appointment.client.user.username}',  # Display the client's name
            'start': f'{appointment.date}T{appointment.start_time}',
            'end': f'{appointment.date}T{appointment.end_time}',
            'client': appointment.client.user.username,  # Client's name
            'service': appointment.service
        })

    return JsonResponse(events, safe=False)


# Hairdresser dashboard
@login_required
def hairdresser_dashboard(request):
    hairdresser = request.user.hairdresser_profile
    appointments = Appointment.objects.filter(hairdresser=hairdresser)  # Appointments only for the current hairdresser
    return render(request, 'hairdressers/hairdresser_dashboard.html', {
        'hairdresser': hairdresser,
        'appointments': appointments
    })




# Hairdresser profile
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

# Custom login redirect
def custom_login_redirect(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'client_profile'):
            return redirect('client_profile')  # Redirect client to profile page
        elif hasattr(request.user, 'hairdresser_profile'):
            return redirect('hairdresser_profile')  # Redirect hairdresser to profile page
    return redirect('home')

# View to get the list of all hairdressers
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
