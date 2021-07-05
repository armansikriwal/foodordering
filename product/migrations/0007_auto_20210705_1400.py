# Generated by Django 3.2.4 on 2021-07-05 08:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]