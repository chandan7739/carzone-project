# Generated by Django 3.1.5 on 2021-07-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('facebook_link', models.URLField(max_length=100)),
                ('twitter_link', models.URLField(max_length=100)),
                ('google_plus', models.URLField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
