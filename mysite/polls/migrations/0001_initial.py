# Generated by Django 3.1 on 2020-08-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=300)),
                ('publish_date', models.DateField()),
                ('product_price', models.FloatField()),
            ],
        ),
    ]
