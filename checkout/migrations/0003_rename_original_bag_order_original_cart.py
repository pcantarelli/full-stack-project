# Generated by Django 3.2.4 on 2021-07-18 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_original_bag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_cart',
        ),
    ]