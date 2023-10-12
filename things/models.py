from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError




# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False
                            )
    description = models.CharField(
        max_length=120,
        unique=False,
        blank=True
                                   )
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(100)])


