from django.db import models
from django.urls import reverse


class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Name")
    address = models.CharField(max_length=200, verbose_name="Address")
    phone_number = models.CharField(max_length=20, verbose_name="Phone number")
    opening_time = models.TimeField(verbose_name="Opening time")
    closing_time = models.TimeField(verbose_name="Closing time")

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shops:detail", kwargs={"shop_name": self.name})
