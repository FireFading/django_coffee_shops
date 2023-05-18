import re

import phonenumbers
from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import CharField, EmailField, EmailInput, ModelForm, PasswordInput, ValidationError
from django.utils.translation import gettext as _
from email_validator import EmailNotValidError, validate_email
from users.models import User


class LoginForm(ModelForm):
    email = EmailField(
        widget=EmailInput,
        error_messages={"required": "Не введен email"},
    )
    password = CharField(
        widget=PasswordInput,
        error_messages={"required": "Не введен password"},
    )

    class Meta:
        model = User
        fields = ("password",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Ваш email", "name": "email"}
        )
        self.fields["password"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Пароль"})

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email):
            raise ValidationError("Такой Email не существует")
        try:
            validate_email(email, check_deliverability=False)
        except Exception as e:
            raise EmailNotValidError("Введен некорректный email") from e
        return email


class SignupForm(ModelForm):
    phone = CharField(
        label="Введите телефон",
        min_length=11,
        max_length=20,
        error_messages={"required": "Необходим номер телефона"},
    )
    email = EmailField(
        label="Введите Email",
        error_messages={"required": "Необходим email"},
        widget=EmailInput,
    )
    password = CharField(
        label="Придумайте пароль",
        widget=PasswordInput,
        error_messages={"required": "Необходим пароль"},
    )
    password2 = CharField(
        label="Повторите пароль",
        widget=PasswordInput,
        error_messages={"required": "Необходимо подтвердить пароль"},
    )

    class Meta:
        model = User
        fields = ("email", "phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Ваш телефон"})
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Ваш email", "name": "email"}
        )
        self.fields["password"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "****"})
        self.fields["password2"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "****"})

    def save(self):
        user = super(SignupForm, self).save()
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    # def clean_phone(self):
    #     phone = self.cleaned_data["phone"].lower()
    #     r = User.objects.filter(phone=phone)
    #     if r.count():
    #         raise ValidationError("Такой телефон уже зарегистрирован")
    #     try:
    #         phone = phonenumbers.parse(phone)
    #         if phonenumbers.is_valid_number(phone) and phonenumbers.is_possible_number(phone):
    #             return (
    #                 phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    #                 .replace(" ", "")
    #                 .replace("-", "")
    #             )
    #         else:
    #             raise ValidationError("Неверный формат телефона")
    #     except Exception as error:
    #         raise ValidationError("Неверный формат телефона") from error

    # def clean_password2(self):
    #     password = self.cleaned_data["password"]
    #     password2 = self.cleaned_data["password2"]
    #     if password != password2:
    #         raise ValidationError("Пароли не совпадают")
    #     try:
    #         re.search(settings.PASS_PATTERN, password)
    #         return password
    #     except Exception as error:
    #         raise ValidationError(
    #             "Длина пароля от 8 до 24 символов. Пароль должен содержать цифры, спецсимволы \
    #             (.,@,_,-,%,$,/,\\,*,!, включая пробел) и латинские буквы верхнего и нижнего регистра."
    #         ) from error

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email):
            raise ValidationError("Такой Email уже зарегистрирован")
        try:
            validate_email(email, check_deliverability=False)
        except Exception as e:
            raise EmailNotValidError("Введен некорректный email") from e
        return email


class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)

    old_password = CharField(
        label=_("Старый пароль"),
        strip=False,
        widget=PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "class": "form-control",
            }
        ),
    )
    new_password1 = CharField(
        label=_("Новый пароль"),
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = CharField(
        label=_("Новый пароль еше раз"),
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    )
