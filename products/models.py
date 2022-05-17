from django.db import models
from django.utils import timezone


class Product(models.Model):

    class ProductStateOpts(models.TextChoices):
        PUBLISH = "PU", "Published"
        DRAFT = "DR", "Draf"
        PRIVATE = "PR", "Private"

    title = models.CharField(max_length=128)
    description = models.TextField(null=True)
    state = models.CharField(max_length=2, default=ProductStateOpts.DRAFT)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
