# Generated by Django 3.0.3 on 2020-02-25 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duties', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('our_offer', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('position', models.CharField(max_length=120)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('vacancy_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
            ],
        ),
    ]
