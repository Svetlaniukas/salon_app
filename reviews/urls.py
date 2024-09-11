# reviews/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('hairdresser/<int:hairdresser_id>/reviews/', views.hairdresser_reviews, name='hairdresser_reviews'),
]
