from django.urls import path

from .views import create_user, my_view_login

urlpatterns = [
    path('register/', create_user, name='register'),
    path('login/', my_view_login, name='login'),
]
