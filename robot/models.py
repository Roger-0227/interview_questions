from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Construct(models.Model):
    name = models.CharField(max_length=50)
    cases = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(101),
        ]
    )
    instructions = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50001),
        ]
    )
    rows = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50001),
        ]
    )
    columns = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50001),
        ]
    )
    start_row = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50001),
        ]
    )
    start_column = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50001),
        ]
    )
    position = models.CharField(max_length=5000)
    result_case = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
