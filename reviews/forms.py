# reviews/forms.py
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # Поля для рейтинга и комментария
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f'{i} stars') for i in range(1, 6)]),  # Выбор оценок от 1 до 5
            'comment': forms.Textarea(attrs={'rows': 3}),  # Текстовое поле для комментария
        }
        


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # Поля, которые будут отображены в форме
