from django.urls import path
from menu.views import CreateProductView, ProductDeleteView, ProductDetailView, ProductsListView, ProductUpdateView

app_name = "menu"

urlpatterns = [
    path("", ProductsListView.as_view(), name="catalog"),
    path("new/", CreateProductView.as_view(), name="new"),
    path("<str:product_name>/", ProductDetailView.as_view(), name="detail"),
    path("edit/<str:product_name>/", ProductUpdateView.as_view(), name="edit"),
    path("delete/<str:product_name>/", ProductDeleteView.as_view(), name="delete"),
]
