# Generated by Django 3.2.4 on 2021-07-03 14:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("doodles", "0002_auto_20210702_1842"),
    ]

    operations = [
        migrations.AddField(
            model_name="doodles",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doodles",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
