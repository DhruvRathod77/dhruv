# Generated by Django 3.2.7 on 2022-09-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deleted',
            field=models.IntegerField(default=0),
        ),
    ]
