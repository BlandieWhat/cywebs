# Generated by Django 3.1 on 2021-02-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announce', models.TextField()),
                ('file', models.FileField(upload_to='media')),
            ],
        ),
    ]
