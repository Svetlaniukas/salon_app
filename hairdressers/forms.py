from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hairdresser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class HairdresserForm(forms.ModelForm):
    class Meta:
        model = Hairdresser
        fields = ['name', 'email', 'phone', 'specialization', 'experience', 'avatar']  


class RatingFilterForm(forms.Form):
    MIN_RATING_CHOICES = [(i, f'{i} stars and up') for i in range(1, 6)]

    min_rating = forms.ChoiceField(
        choices=MIN_RATING_CHOICES,
        required=False,
        label='Minimum Rating',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
