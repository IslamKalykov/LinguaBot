from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
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


@login_required(login_url='login')  # Redirect to login page if not logged in
def user_profile(request):
    return render(request, 'users/user_profile.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('user_profile')  # Redirect to user profile if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')