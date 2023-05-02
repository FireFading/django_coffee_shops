from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls", namespace="base")),
    path("catalog/", include("menu.urls", namespace="menu")),
    path("shops/", include("shops.urls", namespace="shops")),
    path("users/", include("users.urls", namespace="users")),
    path("reviews/", include("reviews.urls", namespace="reviews")),
    path("recipes/", include("recipes.urls", namespace="recipes")),
]
