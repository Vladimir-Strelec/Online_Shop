from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from .forms import PaymentForm
import uuid


def home_view(request):
    return render(request, 'base.html', {})


def painting_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = PaymentForm()

    return render(request, "web/payment.html", {"form": form})


def view_that_asks_for_money(request):
    # What you want the button to do.
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "web/payment.html", context)
