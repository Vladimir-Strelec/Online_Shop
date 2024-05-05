from django.urls import path

from .views import create_user, UserLoginView

urlpatterns = [
    path('register/', create_user, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
