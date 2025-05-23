# Generated by Django 5.2 on 2025-04-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClassificationEvent",
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
                ("source", models.CharField(max_length=256)),
                ("date_time", models.DateTimeField(auto_now=True)),
                ("model_name", models.CharField(blank=True, max_length=256, null=True)),
                ("classification", models.JSONField()),
            ],
        ),
    ]
