from django.db import models
from django.utils import timezone
from menu.models import MenuItem
from users.models import User


class Review(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="comments", verbose_name="Menu Item")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User", related_name="comments")
    text = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created at")

    def __str__(self):
        return f"{self.text[:50]}..."


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    summary = models.CharField(max_length=200, verbose_name="Summary")
    text = models.TextField(verbose_name="Question")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created at")

    def __str__(self):
        return f"{self.text[:50]}..."
