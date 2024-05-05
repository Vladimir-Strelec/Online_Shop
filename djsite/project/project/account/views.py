import random
import string

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import ShopUser


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
            user = ShopUser.objects.create(username=client_numer, email=email, password=password1)
            user.set_password(password1)
            user.save()

            return redirect('home')

    form = RegisterUserForm()
    return render(request, 'account/register-user.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()