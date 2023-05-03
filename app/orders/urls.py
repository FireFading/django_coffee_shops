from django.urls import path
from orders.views import CartView, add_product, create_order, remove_product, remove_products

app_name = "orders"

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("add_product/<int:product_id>/<path:next>/", add_product, name="add_product"),
    path(
        "remove_product/<int:product_id>/<path:next>/",
        remove_product,
        name="remove_product",
    ),
    path(
        "remove_products/<int:product_id>/<path:next>/",
        remove_products,
        name="remove_products",
    ),
    path("create_order/", create_order, name="order"),
]
