# Generated by Django 5.1.3 on 2024-11-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0019_priceshop"),
    ]

    operations = [
        migrations.CreateModel(
            name="PriceBlog",
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
                ("title", models.CharField(max_length=155, verbose_name="Заголовка")),
                ("price", models.IntegerField(verbose_name="Цена")),
                (
                    "image",
                    models.ImageField(upload_to="priceshop", verbose_name="Фото"),
                ),
            ],
            options={
                "verbose_name_plural": "Блог Магазин",
            },
        ),
    ]
