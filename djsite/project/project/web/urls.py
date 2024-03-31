from django.urls import path
from .views import __index__, create_order

urlpatterns = [
    path('', __index__, name='index'),
    path('order/create/', create_order, name='create_order'),
]
