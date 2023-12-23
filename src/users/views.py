# users/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на имя вашей домашней страницы
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
