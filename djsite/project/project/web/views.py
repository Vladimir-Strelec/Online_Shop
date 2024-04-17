from django.shortcuts import render

from .forms import PaymentForm


def painting_payment(request):
    form = PaymentForm()
    return render(request, "payment.html", {"form": form})
