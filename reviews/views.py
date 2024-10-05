from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from hairdressers.models import Hairdresser
from django.contrib.auth.decorators import login_required


def hairdresser_reviews(request, hairdresser_id):
    hairdresser = Hairdresser.objects.get(id=hairdresser_id)  # Get the hairdresser object
    reviews = Review.objects.filter(hairdresser=hairdresser)  # Filter reviews for this specific hairdresser

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.client = request.user  # Assign the current user as the client
            review.hairdresser = hairdresser  # Assign the current hairdresser
            review.save()
            return redirect('hairdresser_reviews', hairdresser_id=hairdresser.id)  # Redirect to the reviews page
    else:
        form = ReviewForm()

    return render(request, 'reviews/hairdresser_reviews.html', {
        'hairdresser': hairdresser,
        'reviews': reviews,  # Pass only the reviews for the specific hairdresser
        'form': form
    })


@login_required
def create_review(request, hairdresser_id):
    hairdresser = get_object_or_404(Hairdresser, id=hairdresser_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.client = request.user  # Assign the User object
            review.hairdresser = hairdresser
            review.save()
            return redirect('hairdresser_reviews', hairdresser_id=hairdresser.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/hairdresser_reviews.html', {
        'hairdresser': hairdresser,
        'form': form
    })
