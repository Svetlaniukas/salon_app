from django.contrib import admin
from django.urls import path, include
from clients import views as client_views
from hairdressers import views as hairdresser_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('clients/', include('clients.urls')),  # Clients app routes
    path('hairdressers/', include('hairdressers.urls')),  # Hairdressers app routes
    path('appointments/', include('appointments.urls')),  # Appointments app routes
    path('register/', client_views.register_client, name='register'),  # Registration for clients
    path('register_hairdresser/', hairdresser_views.register_hairdresser, name='register_hairdresser'),  # Registration for hairdressers
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in authentication routes
    path('', hairdresser_views.home, name='home'),  # Home page
    path('login-redirect/', client_views.custom_login_redirect, name='custom_login_redirect'),  # Redirect after login
    path('reviews/', include('reviews.urls')),  # Connecting the reviews app

    # Password reset routes
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Profile routes
    path('client/profile/', client_views.client_profile, name='client_profile'),  # Client profile
    path('hairdresser/profile/', hairdresser_views.hairdresser_profile, name='hairdresser_profile'),  # Hairdresser profile
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Handle media files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Handle static files
