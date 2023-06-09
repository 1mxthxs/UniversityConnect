# Generated by Django 4.2.1 on 2023-06-25 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Formacao",
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
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="NivelCurso",
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
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Curso",
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
                ("titulo", models.CharField(max_length=100)),
                ("descricao", models.TextField()),
                ("carga_horaria", models.IntegerField()),
                ("tempo_curso", models.CharField(max_length=100)),
                ("mensalidade", models.DecimalField(decimal_places=2, max_digits=8)),
                ("tipo_aula", models.CharField(max_length=100)),
                ("botao", models.CharField(max_length=100)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UniversityConnect.categoria",
                    ),
                ),
                (
                    "formacao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UniversityConnect.formacao",
                    ),
                ),
                (
                    "nivel_curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UniversityConnect.nivelcurso",
                    ),
                ),
            ],
        ),
    ]
