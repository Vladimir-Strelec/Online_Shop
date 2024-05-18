from django.urls import path
from django.views.generic import TemplateView

from .views import create_user, my_view_login, LogOutUser, verifyEmailView

urlpatterns = [
    path('register/', create_user, name='register'),
    path('login/', my_view_login, name='login'),
    path('logout/<int:pk>/', LogOutUser.as_view(), name='logout'),

    path('confirm_email/', TemplateView.as_view(template_name='email-verify/confirm_email.html'), name='confirm_amail'),
    path('verify_email/<uidb64>/<token>/', verifyEmailView, name='verify_email'),
]
