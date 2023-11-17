# Generated by Django 4.2.7 on 2023-11-16 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polyconnmain", "0010_remove_reservation_participants_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="participants",
        ),
        migrations.CreateModel(
            name="UserEvent",
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
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polyconnmain.event",
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
            options={
                "unique_together": {("user", "event")},
            },
        ),
        migrations.AddField(
            model_name="event",
            name="participants",
            field=models.ManyToManyField(
                through="polyconnmain.UserEvent", to="polyconnmain.user"
            ),
        ),
    ]
