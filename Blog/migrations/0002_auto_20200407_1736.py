# Generated by Django 2.0.7 on 2020-04-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
