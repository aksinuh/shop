# Generated by Django 5.0.6 on 2024-06-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_detail_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]
