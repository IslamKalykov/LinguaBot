# Generated by Django 5.0 on 2023-12-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_word"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
            ],
        ),
        migrations.AddField(
            model_name="word",
            name="categories",
            field=models.ManyToManyField(to="users.category"),
        ),
    ]
