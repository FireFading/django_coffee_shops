from celery import shared_task
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from users.models import User
from users.utils import account_activation_token


@shared_task(name="account_activate")
def send_mail(request, data, user: User):
    email = data.get("email")
    current_site = get_current_site(request)
    subject = f"Subscribe on {current_site}"
    message = render_to_string(
        "email/account_activation.html",
        {
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user=user),
        },
    )
    send_email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
    )
    if send_email.send():
        return f"/accounts/login/?command=verification&email={email}"
