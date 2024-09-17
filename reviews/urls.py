from django.urls import path
from . import views

urlpatterns = [
    path('hairdresser/<int:hairdresser_id>/reviews/', views.hairdresser_reviews, name='hairdresser_reviews'),
    path('hairdresser/<int:hairdresser_id>/reviews/create/', views.create_review, name='create_review'),  # Маршрут для создания отзыва
]
