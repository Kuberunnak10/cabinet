from django.urls import path

from users.views import register, home_page, profile

urlpatterns = [
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile')
]