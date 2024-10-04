# Generated by Django 5.1.1 on 2024-10-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_item', '0002_cartitem_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
