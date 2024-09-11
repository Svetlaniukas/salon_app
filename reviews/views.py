# reviews/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from hairdressers.models import Hairdresser

def hairdresser_reviews(request, hairdresser_id):
    hairdresser = Hairdresser.objects.get(id=hairdresser_id)  # Получаем только парикмахера
    reviews = Review.objects.filter(hairdresser=hairdresser)  # Фильтруем отзывы для этого парикмахера

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.client = request.user  # Присваиваем текущего пользователя как клиента
            review.hairdresser = hairdresser  # Присваиваем текущего парикмахера
            review.save()
            return redirect('hairdresser_reviews', hairdresser_id=hairdresser.id)  # Перенаправляем на страницу отзывов
    else:
        form = ReviewForm()

    return render(request, 'reviews/hairdresser_reviews.html', {
        'hairdresser': hairdresser,
        'reviews': reviews,  # Передаем только отзывы для конкретного парикмахера
        'form': form
    })
