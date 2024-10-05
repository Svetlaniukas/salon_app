from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment
from clients.models import Client
from hairdressers.models import Hairdresser
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm

@login_required
def appointment_list(request):
    """Returns a list of all appointments for the calendar"""
    appointments = Appointment.objects.all()
    events = []

    for appointment in appointments:
        events.append({
            'title': f'{appointment.client.user.username} - {appointment.hairdresser.user.username}',
            'start': f'{appointment.date}T{appointment.start_time}',
            'end': f'{appointment.date}T{appointment.end_time}',
        })

    return JsonResponse(events, safe=False)


from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

def create_appointment(request):
    """Creates a new appointment based on POST data"""
    if request.method == 'POST':
        service = request.POST.get('service')
        start = request.POST.get('start')
        end = request.POST.get('end')
        hairdresser_id = request.POST.get('hairdresser')

        # Ensure that both start and end times are provided
        if not start or not end:
            return JsonResponse({'status': 'error', 'message': 'Date and time are required'})

        try:
            hairdresser = Hairdresser.objects.get(id=hairdresser_id)
            client = request.user.client_profile  # Get the logged-in client's profile

            # Create the appointment
            appointment = Appointment.objects.create(
                client=client,
                hairdresser=hairdresser,
                service=service,
                date=start.split('T')[0],  # Extract the date part
                start_time=start.split('T')[1],
                end_time=end.split('T')[1]
            )

            # After successful creation, redirect the user
            return HttpResponseRedirect(reverse('client_dashboard'))  # Change to the appropriate route
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def update_appointment(request):
    """Updates an existing appointment"""
    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('id')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.service = request.POST.get('service')
            
            # Ensure both start_time and end_time are received and updated
            appointment.start_time = request.POST.get('start')
            appointment.end_time = request.POST.get('end')

            appointment.save()
            return JsonResponse({'status': 'success'})
        except Appointment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Appointment not found'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
def delete_appointment(request):
    """Deletes an appointment based on POST data"""
    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('id')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return JsonResponse({'status': 'success'})
        except Appointment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Appointment not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
