from django.contrib import admin
from django.urls import path, include
from clients import views as client_views
from hairdressers import views as hairdresser_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Routes for the clients app
    path('clients/', include('clients.urls')),
    
    # Routes for the hairdressers app
    path('hairdressers/', include('hairdressers.urls')),
    
    # Routes for the appointments app
    path('appointments/', include('appointments.urls')),

    # Registration for clients and hairdressers
    path('register/', client_views.register_client, name='register'),  # Client registration
    path('register_hairdresser/', hairdresser_views.register_hairdresser, name='register_hairdresser'),  # Hairdresser registration

    # Authentication routes (Django built-in views)
    path('accounts/', include('django.contrib.auth.urls')),

    # Home page
    path('', hairdresser_views.home, name='home'),

    # Redirect after login
    path('login-redirect/', client_views.custom_login_redirect, name='custom_login_redirect'),

    # Routes for the reviews app
    path('reviews/', include('reviews.urls')),

    # Password reset routes (Django built-in views)
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Client and hairdresser profile routes
    path('client/profile/', client_views.client_profile, name='client_profile'),  # Client profile
    path('hairdresser/profile/', hairdresser_views.hairdresser_profile, name='hairdresser_profile'),  # Hairdresser profile
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files during development (optional, generally handled by WhiteNoise in production)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
