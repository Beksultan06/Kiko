# Generated by Django 5.1.3 on 2024-11-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="settings",
            name="image",
            field=models.ImageField(
                default=1, upload_to="settings", verbose_name="Фото"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="image2",
            field=models.ImageField(
                default=1, upload_to="settings", verbose_name="Фото Предложения"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="image3",
            field=models.ImageField(
                default=1, upload_to="settings", verbose_name="Фото курсов - 1"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="image4",
            field=models.ImageField(
                default=1, upload_to="settings", verbose_name="Фото курсов - 2"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="image5",
            field=models.ImageField(
                default=1, upload_to="settings", verbose_name="Фото Цены"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="image6",
            field=models.ImageField(
                default=1, upload_to="settings", verbose_name="Фото рекомендации"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="image7",
            field=models.ImageField(
                default=1,
                upload_to="settings",
                verbose_name="Фото Детального просмотра",
            ),
            preserve_default=False,
        ),
    ]
