from django.urls import path, include

from .views import home_view, painting_payment

urlpatterns = (
    path("", home_view, name='home'),
    path('paypal/', painting_payment, name='payment'),

)

