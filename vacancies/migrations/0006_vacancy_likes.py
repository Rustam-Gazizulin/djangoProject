# Generated by Django 4.1.1 on 2022-10-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_skill_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
