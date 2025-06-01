from django.db import models
from django.contrib.auth.models import User


class Measurement(models.Model):
    STATUS_CHOICES = [
        ("created", "Created"),
        ("processing", "Processing"),
        ("finished", "Finished"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="measurements",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="created")
    body_fat_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        default=None,
    )  # calculated by our IA model
    biceps_circumference = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=0,
    )  # calculated by our IA model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
