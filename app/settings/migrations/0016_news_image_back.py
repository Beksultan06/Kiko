# Generated by Django 5.1.3 on 2024-11-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0015_news"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="image_back",
            field=models.ImageField(default=1, upload_to="Фото на заднем фоне"),
            preserve_default=False,
        ),
    ]
