from django.urls import path

from .views import home_view, painting_payment

urlpatterns = (
    path("", home_view, name='home'),
    path("pay/", painting_payment, name='payment'),
)

