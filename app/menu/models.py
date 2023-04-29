from django.db import models
from shops.models import Shop


class MenuItem(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)
    price = models.FloatField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="menu_items")

    def __str__(self):
        return f"{self.name} :: {self.shop}"
