# Generated by Django 5.0.6 on 2024-06-23 02:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_detail_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produc', to='products.color'),
        ),
    ]