from django.db import models
from shops.models import Shop


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", unique=True)
    price = models.FloatField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="menu_items", verbose_name="Shop")

    def __str__(self):
        return f"{self.name} :: {self.shop}"
