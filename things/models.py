from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator




# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False
        )
    description = models.CharField(
        max_length=120,
        blank=True,
        unique=False
    )
    quantity = models.PositiveIntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(100)])