from django.urls import path
from menu.views import CreateProductView, HomeView, ProductDetailView, ProductsListView

app_name = "coffee"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("catalog/", ProductsListView.as_view(), name="catalog"),
    path("catalog/new/", CreateProductView.as_view(), name="new"),
    path("catalog/<str:product_name>", ProductDetailView.as_view(), name="detail"),
]
