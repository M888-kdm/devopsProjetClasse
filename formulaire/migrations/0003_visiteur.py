# Generated by Django 4.2.4 on 2023-09-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formulaire", "0002_endpointvisitor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visiteur",
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
                ("url", models.CharField(max_length=255, unique=True)),
                ("compteur", models.IntegerField(default=0)),
            ],
        ),
    ]
