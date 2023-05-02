from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView, View
from django.views.generic.edit import FormView, UpdateView
from users.forms import LoginForm, SignupForm, UserPasswordChangeForm
from users.models import User
from users.tasks import send_mail
from users.utils import account_activation_token


def account_activate(request, uidb64, token, backend="django.contrib.auth.backends.ModelBackend"):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as error:
        print(f"Error to find user: {error}")
        user = None
    if user is None or not account_activation_token.check_token(user, token):
        messages.error(request, "Invalid link. Please, try again")
        return render(request, "users/account_activation_invalid.html")
    user.is_active = True
    user.save()
    messages.success(request, "Your account has been activated")
    login(request, user, backend=backend)
    return redirect("base:home")


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("base:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        if user is None or not user.is_active:
            return self.form_invalid(form)
        messages.success(self.request, "Login successful")
        login(self.request, user)
        return redirect(self.success_url)


class SignupView(FormView):
    template_name = "users/register.html"
    form_class = SignupForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        send_mail(self.request, form.cleaned_data, user)
        messages.success(self.request, "Profile successfully created")
        messages.success(self.request, "To your mail send confirmation to activate your account")
        return super(SignupView, self).form_valid(form)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile_edit.html"
    model = User
    fields = ["phone", "email"]
    success_url = reverse_lazy("users:profile_edit")

    def get_object(self):
        return self.request.user


class UserPasswordResetView(PasswordResetView):
    """
    sends email with token
    """

    template_name = "users/password_reset.html"
    email_template_name = ("mail/password_reset.html",)
    success_url = reverse_lazy("users:password_reset_done")
    title = _("Reset password")
    token_generator = default_token_generator


class UserPasswordDoneView(PasswordResetDoneView):
    """
    shows success message for email sending
    """

    template_name = "users/password_reset_done.html"


class UserPasswordConfirmView(PasswordResetConfirmView):
    """
    checks link user clicked and processing new password
    """

    template_name = "users/password_reset_confirm.html"


class UserPasswordCompleteView(PasswordResetCompleteView):
    """
    shows success message for changing new password
    """

    template_name = "users/password_reset_complete.html"


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("base:home")
    template_name = "users/profile_delete_confirm.html"


class ChangePasswordView(LoginRequiredMixin, View):
    template_name = "users/password_change.html"

    def get(self, request):
        form = UserPasswordChangeForm(request.user)
        context = {"form": form}

        return render(request, self.template_name, context)

    def post(self, request):
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            subject = "Password successfully changed"
            current_site = get_current_site(self.request)
            message = render_to_string(
                "mail/change_password.html",
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
                [user.email],
            )
            try:
                send_email.send()
            except Exception as error:
                print(f"Error to send email: {error}")
            messages.success(request, "Password successfully changed")

            return redirect("users:profile_edit")
        else:
            messages.error(request, "Please, correct the form")

        context = {"form": form}

        return render(request, self.template_name, context)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("base:home")
