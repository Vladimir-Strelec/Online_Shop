from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm


class CreateUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register-user.html'
    success_url = reverse_lazy('home')
