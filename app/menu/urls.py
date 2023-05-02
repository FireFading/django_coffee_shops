from django.urls import path
from menu.views import CreateProductView, HomeView, ProductDetailView, ProductsListView, ProductUpdateView, ProductDeleteView

app_name = "menu"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("catalog/", ProductsListView.as_view(), name="catalog"),
    path("catalog/new/", CreateProductView.as_view(), name="new"),
    path("catalog/<str:product_name>/", ProductDetailView.as_view(), name="detail"),
    path("catalog/edit/<str:product_name>/", ProductUpdateView.as_view(), name="edit"),
    path("catalog/delete/<str:product_name>/", ProductDeleteView.as_view(), name="delete"),
]
