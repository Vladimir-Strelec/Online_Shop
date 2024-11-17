from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from .forms import PaymentForm
import uuid


def home_view(request):
    return render(request, 'base.html', {})


def painting_payment(request):
    host = request.get_host()
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": request.user.id,
        "notify_url": 'https://{}{}'.format(host, reverse("paypal-ipn")),
        "return": 'https://{}{}'.format(host, reverse("paypal-ipn")),
        "cancel_return": 'https://{}{}'.format(host, reverse("paypal-ipn")),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    if request.method == 'POST':

        form = PayPalPaymentsForm(initial=paypal_dict)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "web/payment.html", {"form": form})


#def view_that_asks_for_money(request):
    # What you want the button to do.


    # Create the instance.
    #form = PayPalPaymentsForm(initial=paypal_dict)
    #context = {"form": form}
    #return render(request, "web/payment.html", context)
