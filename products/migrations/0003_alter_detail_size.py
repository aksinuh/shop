# Generated by Django 5.0.6 on 2024-05-30 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_detail_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.detail'),
        ),
    ]