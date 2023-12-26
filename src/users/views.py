from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на имя вашей домашней страницы
        else:
            print(form.errors)  # Добавьте эту строку для вывода ошибок в консоль
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def home(request):
    return render(request, 'users/home.html') 


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # После успешной авторизации перенаправьте пользователя на другую страницу
                return redirect('user_profile')  # Замените 'user_profile' на вашу страницу с данными пользователя
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})



@login_required
def user_profile(request):
    return render(request, 'users/user_profile.html')