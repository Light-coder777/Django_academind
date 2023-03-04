# Generated by Django 4.1.7 on 2023-02-26 07:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="is_bestselling",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinLengthValidator(1),
                    django.core.validators.MaxLengthValidator(5),
                ]
            ),
        ),
    ]
