# users/urls.py
from django.urls import path
from .views import register, home, login_view, user_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('user_profile/', user_profile, name='user_profile'),
]
