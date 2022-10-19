# Generated by Django 4.1 on 2022-10-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0005_alter_car_slug_alter_manufacturer_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
