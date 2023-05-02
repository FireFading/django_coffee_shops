from django.urls import path
from shops.views import CreateShopView, ShopDetailView, ShopsListView

app_name = "coffee"

urlpatterns = [
    path("", ShopsListView.as_view(), name="all"),
    path("new/", CreateShopView.as_view(), name="new"),
    path("<str:shop_name>/", ShopDetailView.as_view(), name="detail"),
]
