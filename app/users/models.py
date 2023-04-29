from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models import BooleanField, CharField, EmailField
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_superuser(self, email, phone, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")
        if other_fields.get("is_active") is not True:
            raise ValueError("Superuser must be assigned to is_active=True")

        return self.create_user(email, phone, password, **other_fields)

    def create_user(self, email, phone, password, **other_fields):
        if not email:
            raise ValueError(_("User must have email"))
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = EmailField(unique=True, null=True, verbose_name="Email")
    phone = CharField(max_length=100, blank=True, null=True, verbose_name="Телефон")
    is_active = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return self.email