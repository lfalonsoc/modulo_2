# Generated by Django 4.2.3 on 2023-07-12 10:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("estado", models.BooleanField(default=True)),
                ("titulo", models.CharField(max_length=255)),
                ("head_image", models.ImageField(upload_to="posts/fotos")),
                ("post", ckeditor.fields.RichTextField()),
                ("crear", models.DateTimeField(auto_now_add=True)),
                ("modificar", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ("titulo",),
            },
        ),
    ]