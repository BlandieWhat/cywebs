# Generated by Django 3.2.5 on 2021-07-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_auto_20210721_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='poster',
            field=models.URLField(),
        ),
    ]