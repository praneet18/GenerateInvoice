# Generated by Django 3.1 on 2020-08-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200818_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_mrp',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
