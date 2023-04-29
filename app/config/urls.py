from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("menu.urls", namespace="menu")),
    path("", include("shops.urls", namespace="shops")),
]
