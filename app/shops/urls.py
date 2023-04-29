from django.urls import path
from shops.views import ShopDetailView, ShopsListView

app_name = "coffee"

urlpatterns = [
    path("shops", ShopsListView.as_view(), name="all"),
    path("shops/<str:shop_name>", ShopDetailView.as_view(), name="detail"),
]
