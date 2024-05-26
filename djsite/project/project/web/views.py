from django.shortcuts import render, redirect

from .forms import PaymentForm
from .models import Painting


def home(request):
    return render(request, 'base.html', {})


def painting_payment(request):

    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaymentForm()

    return render(request, "web/payment.html", {"form": form})
