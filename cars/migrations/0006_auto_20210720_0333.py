# Generated by Django 3.1.5 on 2021-07-19 22:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20210719_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 20, 3, 33, 5, 399751)),
        ),
    ]