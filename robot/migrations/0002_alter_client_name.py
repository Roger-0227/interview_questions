# Generated by Django 5.1.2 on 2024-10-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("robot", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
