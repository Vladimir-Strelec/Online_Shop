from distlib.compat import text_type
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings

from .. import settings as settings_impl


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return text_type((user.is_active + user.pk + timestamp))


def send_email_for_verify(request, user_with_id):
    current_site = get_current_site(request)

    context = {
        'user': user_with_id,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user_with_id.id)),
        'token': token_generator.make_token(user_with_id),
    }
    message = render_to_string('email-verify/verify_email.html', context=context)
    email = EmailMessage('Email verify', body=message, from_email=settings_impl.EMAIL_HOST_USER, to=[user_with_id.email])


    email.send()

token_generator = AppTokenGenerator()
