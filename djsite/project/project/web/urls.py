from django.urls import path

from .views import painting_payment

urlpatterns = (
    path("", painting_payment, name='payment'),
)

