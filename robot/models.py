from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cases = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(101),
        ]
    )


class Construct(models.Model):
    name = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="construct_name"
    )
    cases = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="construct_cases"
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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.start_row >= self.rows:
            raise ValidationError("起始行必須小於行數。")
        if self.start_column >= self.columns:
            raise ValidationError("起始列必須小於列數。")
        if not re.match(r"^[NSWE]+$", self.position.upper()):
            raise ValidationError("必須符合字元 (N S W E)")
