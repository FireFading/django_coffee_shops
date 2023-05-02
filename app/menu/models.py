from django.db import models
from shops.models import Shop


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", unique=True)
    description = models.TextField(verbose_name="Description", blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", unique=True)
    price = models.FloatField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="menu_items", verbose_name="Shop")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Category")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-name"]

    def __str__(self):
        return f"{self.name} :: {self.shop}"
