# Generated by Django 4.2.2 on 2023-07-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UniversityConnect", "0002_categoria_name_en_curso_description_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="curso",
            name="image",
            field=models.ImageField(
                blank=True, default="", upload_to="recipes/cover/%Y/%m/%d/"
            ),
        ),
    ]