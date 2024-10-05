from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # Fields for rating and comment
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f'{i} stars') for i in range(1, 6)]),  # Choice of ratings from 1 to 5
            'comment': forms.Textarea(attrs={'rows': 3}),  # Textarea for comment
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # Fields that will be displayed in the form
