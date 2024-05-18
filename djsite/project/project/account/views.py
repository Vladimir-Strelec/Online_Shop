import random
import string

from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import ShopUser
from .utils import send_email_for_verify


def client_numer_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# class CreateUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'register-user.html'
#     success_url = reverse_lazy('home')


def create_user(request):
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


def my_view_login(request):
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

            else:
                return redirect('login')
    return render(request,'account/login.html', {'form': form})


class LogOutUser(LoginRequiredMixin, LogoutView):
    template_name = 'account/login.html'


def verifyEmailView(request):
    u = request
    return u

# def login(request):
#     if request.method == 'POST':
#         form = LoginUserForm(data=request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password1']
#             queryset_user = User.objects.filter(email=email)[0].username
#             username = queryset_user[0].username
#             user = auth.authenticate(username=username, email=email, password=password)
#
#             session_key = request.session['user']
#
#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f"{username}, Вы вошли в аккаунт")
#
#                 if session_key:
#                     User.objects.filter(session_key=session_key).update(user=user)
#
#                 redirect_page = request.POST.get('next', None)
#                 if redirect_page and redirect_page != reverse('user:logout'):
#                     return HttpResponseRedirect(request.POST.get('next'))
#
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = LoginUserForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'account/login.html', context)