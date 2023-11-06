# Generated by Django 4.2.7 on 2023-11-01 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cafe",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("address", models.TextField()),
                ("suitable_for_events", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="District",
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
                ("name", models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("gender", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "nationality",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "german_proficiency_level",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("native_languages", models.JSONField()),
                ("learning_languages", models.JSONField()),
                ("hobbies", models.JSONField()),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polyconnmain.district",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("reservation_date", models.DateTimeField()),
                ("participants", models.JSONField()),
                (
                    "cafe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polyconnmain.cafe",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polyconnmain.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=255)),
                ("event_type", models.CharField(blank=True, max_length=255, null=True)),
                ("date", models.DateTimeField()),
                ("participants", models.JSONField()),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polyconnmain.district",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cafe",
            name="district",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="polyconnmain.district"
            ),
        ),
    ]
