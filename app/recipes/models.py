from django.db import models
from menu.models import Product
from users.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    products = models.ManyToManyField(Product, related_name="recipes", verbose_name="Products")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes", verbose_name="User")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
