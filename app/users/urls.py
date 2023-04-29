from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import (
    ChangePasswordView,
    DeleteUserView,
    LoginView,
    ProfileEditView,
    SignupView,
    UserPasswordCompleteView,
    UserPasswordConfirmView,
    UserPasswordDoneView,
    UserPasswordResetView,
    account_activate,
)

app_name = "accounts"

urlpatterns = [
    path("", ProfileEditView.as_view(), name="profile_edit"),
    path("register/", SignupView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("activate/<slug:uidb64>/<slug:token>/", account_activate, name="activate"),
    path("password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        UserPasswordDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>",
        UserPasswordConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        UserPasswordCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("password_change", ChangePasswordView.as_view(), name="password_change"),
    path("delete/<int:pk>", DeleteUserView.as_view(), name="delete_profile"),
]
