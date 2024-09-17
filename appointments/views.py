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
    """Возвращает список всех записей для календаря"""
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
    if request.method == 'POST':
        service = request.POST.get('service')
        start = request.POST.get('start')
        end = request.POST.get('end')
        hairdresser_id = request.POST.get('hairdresser')

        if not start or not end:
            return JsonResponse({'status': 'error', 'message': 'Date and time are required'})

        try:
            hairdresser = Hairdresser.objects.get(id=hairdresser_id)
            client = request.user.client_profile  # Get the logged-in client's profile

            appointment = Appointment.objects.create(
                client=client,
                hairdresser=hairdresser,
                service=service,
                date=start.split('T')[0],  # Extract date part
                start_time=start.split('T')[1],
                end_time=end.split('T')[1]
            )

            # После успешного создания записи перенаправляем пользователя
            return HttpResponseRedirect(reverse('client_dashboard'))  # Измените на нужный маршрут
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def update_appointment(request):
    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('id')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.service = request.POST.get('service')
            
            # Make sure you are receiving and updating both start_time and end_time
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
    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('id')
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return JsonResponse({'status': 'success'})
        except Appointment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Appointment not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
