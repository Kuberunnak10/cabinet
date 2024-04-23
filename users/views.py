from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request,
                  'registration/registration.html',
                  {'form': form})


def home_page(request):
    return render(request, 'home_page.html')


@login_required(login_url='/users/login')
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.contacts = request.POST.get('contacts')

        new_role = request.POST.get('role')
        user.role = new_role
        if user.role == 'Executor':
            user.experience = request.POST.get('experience')
        user.save()
        return redirect('profile')
    return render(request, 'profile/profile.html')


