# Generated by Django 4.2.4 on 2023-09-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formulaire", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EndpointVisitor",
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
                ("endpoint_name", models.CharField(max_length=100, unique=True)),
                ("visitor_count", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
