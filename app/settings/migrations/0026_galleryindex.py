# Generated by Django 5.1.3 on 2024-12-02 07:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0025_kikoupdate_descriptions_en_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryIndex",
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
                (
                    "image1",
                    models.ImageField(upload_to="settings", verbose_name="Фото 1"),
                ),
                (
                    "image2",
                    models.ImageField(upload_to="settings", verbose_name="Фото 2"),
                ),
                (
                    "image3",
                    models.ImageField(upload_to="settings", verbose_name="Фото 3"),
                ),
                (
                    "image4",
                    models.ImageField(upload_to="settings", verbose_name="Фото 4"),
                ),
                ("title", models.CharField(max_length=155, verbose_name="Заголовка")),
                (
                    "title2",
                    models.CharField(max_length=155, verbose_name="Заголовка 2"),
                ),
                (
                    "descriptions",
                    ckeditor.fields.RichTextField(verbose_name="Описание"),
                ),
                (
                    "title2_2",
                    models.CharField(max_length=155, verbose_name="Заголовка"),
                ),
                (
                    "title2_1",
                    models.CharField(max_length=155, verbose_name="Заголовка 2"),
                ),
                (
                    "descriptions2",
                    ckeditor.fields.RichTextField(verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name_plural": "Галлерия на Главной странице",
            },
        ),
    ]