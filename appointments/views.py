from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment
from clients.models import Client
from hairdressers.models import Hairdresser
from datetime import datetime
from django.contrib.auth.decorators import login_required

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

@csrf_exempt
def create_appointment(request):
    if request.method == 'POST':
        try:
            client = request.user.client_profile  # Получаем профиль клиента
            service = request.POST.get('service')
            start = request.POST.get('start')
            end = request.POST.get('end')
            hairdresser_id = request.POST.get('hairdresser')

            start_datetime = datetime.fromisoformat(start)
            end_datetime = datetime.fromisoformat(end)
            hairdresser = Hairdresser.objects.get(id=hairdresser_id)

            # Создание новой записи
            Appointment.objects.create(
                client=client,
                hairdresser=hairdresser,
                service=service,
                date=start_datetime.date(),
                start_time=start_datetime.time(),
                end_time=end_datetime.time()
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})