# Generated by Django 5.1.3 on 2024-11-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assist", "0002_rename_institutionnames_institutionname"),
    ]

    operations = [
        migrations.CreateModel(
            name="AcademicYear",
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
                ("fall_year", models.IntegerField(default=0)),
            ],
        ),
    ]
