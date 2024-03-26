from django.http import HttpResponse
from django.shortcuts import render


def __index__(request):
    return HttpResponse('Main site')


def categories(request, slug):
    print(request.GET)
    return HttpResponse('TEST')
