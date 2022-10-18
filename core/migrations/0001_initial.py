# Generated by Django 4.1.2 on 2022-10-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(blank=True, max_length=50)),
                ("logo", models.ImageField(blank=True, null=True, upload_to="")),
                ("summary", models.TextField(blank=True, null=True)),
                ("href", models.URLField(blank=True, null=True)),
            ],
        ),
    ]