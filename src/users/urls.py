# users/urls.py
from django.urls import path
from .views import register, home, login_view, user_profile, logout_view, get_random_word

urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_profile/', user_profile, name='user_profile'),
    path('get_random_word/', get_random_word, name='get_random_word'),
]
