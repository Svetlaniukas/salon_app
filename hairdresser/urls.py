from django.contrib import admin
from django.urls import path, include
from clients import views as client_views
from hairdressers import views as hairdresser_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('hairdressers/', include('hairdressers.urls')),
    path('appointments/', include('appointments.urls')),
    path('register/', client_views.register_client, name='register'),
    path('register_hairdresser/', hairdresser_views.register_hairdresser, name='register_hairdresser'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', client_views.home, name='home'),
    path('login-redirect/', client_views.custom_login_redirect, name='custom_login_redirect'),

    # Восстановление пароля
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Профили
    path('client/profile/', client_views.client_profile, name='client_profile'),
    path('hairdresser/profile/', hairdresser_views.hairdresser_profile, name='hairdresser_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
