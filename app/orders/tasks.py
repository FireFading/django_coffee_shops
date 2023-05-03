from celery import shared_task
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@shared_task(name="send_mail_confirm_order")
def send_mail_confirm_order(order, request):
    subject = "Your order is confirmed"
    current_site = get_current_site(request)
    message = render_to_string(
        "mail/order_status_update.html",
        {
            "domain": current_site.domain,
            "total_price": order.total_price,
            "items": order.items,
        },
    )
    send_email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    if send_email.send():
        messages.success(request, "Mail with your order details has been sent successfully")


@shared_task(name="send_email_order_to_admin")
def send_mail_order_to_admin(order):
    subject = "Новый заказ"
    message = render_to_string(
        "mail/order_to_admin.html",
        {"items": order.items, "total_price": order.total_price, "user": order.user},
    )
    send_email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_ADMIN],
    )
    send_email.send()
