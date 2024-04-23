from django.urls import path

from users.views import register, profile

urlpatterns = [
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile'),

]