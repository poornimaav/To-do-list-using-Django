# Generated by Django 4.2.2 on 2023-06-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
