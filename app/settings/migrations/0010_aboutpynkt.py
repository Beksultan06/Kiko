# Generated by Django 5.1.3 on 2024-11-28 16:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0009_about_descriptions_about_about_image_abotu_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutPynkt",
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
                (
                    "descriptions",
                    ckeditor.fields.RichTextField(verbose_name="Описание"),
                ),
                ("number", models.IntegerField(verbose_name="Нумерация")),
                ("plus1", models.CharField(max_length=155, verbose_name="Плюсы 1 ")),
                ("plus2", models.CharField(max_length=155, verbose_name="Плюсы 2 ")),
            ],
            options={
                "verbose_name_plural": "Пункты О нас",
            },
        ),
    ]
