# Generated by Django 3.2.6 on 2021-08-02 21:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=10)),
                ('varietal', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 8, 2, 21, 57, 56, 958170, tzinfo=utc))),
            ],
        ),
    ]
