from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('role', 'username', 'name')
        # fields = ('username', 'name', 'email', 'contacts', 'role', 'experience',)


class ExecutorProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'contacts', 'experience', 'role']


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'contacts', 'role']

