# Generated by Django 3.0.3 on 2020-02-25 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vacancy',
            new_name='Listing',
        ),
        migrations.RenameModel(
            old_name='Requirements',
            new_name='Requirement',
        ),
    ]