# Generated by Django 5.2.1 on 2025-05-19 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modelos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="musician",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firts_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("instrument", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
                ("num_stars", models.IntegerField()),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modelos.musician",
                    ),
                ),
            ],
        ),
    ]
