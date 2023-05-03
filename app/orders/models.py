from django.db import models
from users.models import User


class Order(models.Model):
    ORDER_STATUSES = [
        ("CREATED", "Created"),
        ("PENDED", "Pended"),
        ("COMPLETED", "Completed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", verbose_name="User")
    message = models.TextField(blank=True, null=True, verbose_name="Comment to order")
    total_price = models.FloatField(default=0, verbose_name="Total price")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Updated time")
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUSES,
        default="CREATED",
        verbose_name="Status",
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ("-created_time",)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="Order")
    product = models.CharField(max_length=255, verbose_name="Product in order")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = "Product in order"
        verbose_name_plural = "Products in order"
