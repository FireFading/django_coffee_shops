from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон")
    opening_time = models.TimeField(verbose_name="Время открытия")
    closing_time = models.TimeField(verbose_name="Время закрытия")

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"
        ordering = ["-name"]

    def __str__(self):
        return self.name
