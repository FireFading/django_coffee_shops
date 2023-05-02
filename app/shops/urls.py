from django.urls import path
from shops.views import CreateShopView, ShopDetailView, ShopsListView, ShopUpdateView, ShopDeleteView

app_name = "shops"

urlpatterns = [
    path("", ShopsListView.as_view(), name="all"),
    path("new/", CreateShopView.as_view(), name="new"),
    path("<str:shop_name>/", ShopDetailView.as_view(), name="detail"),
    path("edit/<str:shop_name>/", ShopUpdateView.as_view(), name="edit"),
    path("delete/<str:shop_name>/", ShopDeleteView.as_view(), name="delete"),
]
