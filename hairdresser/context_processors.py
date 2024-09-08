# hairdresser/context_processors.py

def user_role(request):
    if request.user.is_authenticated:
        return {
            'is_client': hasattr(request.user, 'client_profile'),
            'is_hairdresser': hasattr(request.user, 'hairdresser_profile'),
        }
    return {}
