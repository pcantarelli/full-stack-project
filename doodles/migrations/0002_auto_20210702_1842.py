# Generated by Django 3.2.4 on 2021-07-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doodles", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="doodles",
            options={"verbose_name_plural": "Doodles"},
        ),
        migrations.AlterField(
            model_name="doodles",
            name="time_to_complete",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
