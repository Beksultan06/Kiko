# Generated by Django 5.1.3 on 2024-11-28 16:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0010_aboutpynkt"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="gallery", verbose_name="Фото")),
                (
                    "title_gellary",
                    ckeditor.fields.RichTextField(verbose_name="Заголовка"),
                ),
                (
                    "title_discounts",
                    models.CharField(max_length=155, verbose_name="Заголовка скидки"),
                ),
                (
                    "title_Discounts_Available",
                    models.CharField(
                        max_length=155, verbose_name="Заголовка Доступные скидки"
                    ),
                ),
                (
                    "descriptions_discounts",
                    ckeditor.fields.RichTextField(verbose_name="Описание"),
                ),
                (
                    "image_discounts",
                    models.ImageField(upload_to="gallery", verbose_name="Фото скидки"),
                ),
            ],
            options={
                "verbose_name_plural": "Галлерия",
            },
        ),
    ]
