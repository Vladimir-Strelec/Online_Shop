from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateOrder


def __index__(request):

    return HttpResponse(request)


def create_order(request):
    form = CreateOrder(request.GET)
    if request.method == 'POST':
        form = CreateOrder(request.POST)
        if form.is_valid():
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'create_order.html', context)

