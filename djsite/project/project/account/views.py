import random
import string

from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import ShopUser
from .utils import send_email_for_verify
from ..mixins.mixin_view import RedirectToHome


def client_numer_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_user(request):
    """call the dispatch method"""
    # RedirectToHome()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        client_numer = client_numer_generator()
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if form.is_valid() and password1 == password2:
            user = User.objects.create(username=client_numer, email=email, password=password1)
            user.set_password(password1)
            user.save()
            send_email_for_verify(request, user)

            return redirect('home')

    form = RegisterUserForm()
    return render(request, 'account/register-user.html', {'form': form})


def login_user(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        user_from_data = (User.objects.filter(email=request.POST['email']))
        if form.is_valid() and user_from_data:

            email = request.POST["email"]
            password = request.POST["password"]
            username = User.objects.filter(email=email)[0].username
            user = authenticate(request, username=username, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        form = LoginUserForm()
        form.errors[''] = 'Check the correctness of your login or password'

    return render(request,'account/login.html', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You are logged out")
        return redirect('home')
    return render(request, 'account/logout.html', {})


def verify_email_view(request, uidb64, token):
    u = request
    return u

