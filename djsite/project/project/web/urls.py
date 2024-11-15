from django.urls import path, include

from .views import home_view, view_that_asks_for_money, painting_payment

urlpatterns = (
    path("", home_view, name='home'),
    path('payment/', painting_payment, name='payment'),
)

