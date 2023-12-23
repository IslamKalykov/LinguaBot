# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ('full_name', 'phone_number', 'username', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Добавьте свои собственные проверки номера телефона при необходимости
        return phone_number
