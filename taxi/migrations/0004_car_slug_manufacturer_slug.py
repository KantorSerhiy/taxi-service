# Generated by Django 4.1 on 2022-10-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0003_alter_driver_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="slug",
            field=models.SlugField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="manufacturer",
            name="slug",
            field=models.SlugField(default="", max_length=255),
        ),
    ]