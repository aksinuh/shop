# Generated by Django 5.0.6 on 2024-06-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_detail_discount_alter_detail_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
    ]
