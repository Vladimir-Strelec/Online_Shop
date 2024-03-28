from django.http import HttpResponse
from django.shortcuts import render

from .forms import CreateOrder


def __index__(request):
    return HttpResponse('Main site')


def create_order(request):
    form = CreateOrder(request.GET)
    context = {
        'form': form
    }
    return render(request, 'create_order.html', context)

