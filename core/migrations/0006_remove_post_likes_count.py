# Generated by Django 4.1.6 on 2023-02-20 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes_count',
        ),
    ]
