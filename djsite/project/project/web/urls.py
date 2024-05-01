from django.urls import path

from .views import home, painting_payment

urlpatterns = (
    path("", home, name='home'),
    path("pay/", painting_payment, name='payment'),
)

