# Generated by Django 4.2.15 on 2024-08-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companyApp", "0015_remove_blog_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="author",
            field=models.CharField(default="name", max_length=100),
        ),
    ]
