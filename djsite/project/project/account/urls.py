from django.urls import path
from django.views.generic import TemplateView

from .views import create_user, login_user, logout_user, verify_email_view

urlpatterns = [
    path('', create_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('confirm_email/', TemplateView.as_view(template_name='email-verify/confirm_email.html'), name='confirm_amail'),
    path('verify_email/<uidb64>/<token>/', verify_email_view, name='verify_email'),
]
