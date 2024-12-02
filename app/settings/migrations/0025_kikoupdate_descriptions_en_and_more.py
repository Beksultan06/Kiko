# Generated by Django 5.1.3 on 2024-11-30 17:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0024_remove_settings_descriptions_courses_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="kikoupdate",
            name="descriptions_en",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="Описание"),
        ),
        migrations.AddField(
            model_name="kikoupdate",
            name="descriptions_ru",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="Описание"),
        ),
        migrations.AddField(
            model_name="kikoupdate",
            name="title_en",
            field=models.CharField(max_length=155, null=True, verbose_name="Заголовка"),
        ),
        migrations.AddField(
            model_name="kikoupdate",
            name="title_ru",
            field=models.CharField(max_length=155, null=True, verbose_name="Заголовка"),
        ),
    ]