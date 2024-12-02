# Generated by Django 5.1.3 on 2024-11-26 14:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0002_settings_image_settings_image2_settings_image3_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image1", models.ImageField(upload_to="image", verbose_name="Фото 1")),
                ("image2", models.ImageField(upload_to="image", verbose_name="Фото 2")),
            ],
            options={
                "verbose_name_plural": "Галлерия",
            },
        ),
        migrations.AlterField(
            model_name="settings",
            name="title",
            field=ckeditor.fields.RichTextField(verbose_name="Заголовка"),
        ),
    ]
