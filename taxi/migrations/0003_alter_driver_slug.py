# Generated by Django 4.1 on 2022-10-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_driver_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]