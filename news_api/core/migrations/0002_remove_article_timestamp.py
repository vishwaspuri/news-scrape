# Generated by Django 3.0.4 on 2020-03-18 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='timestamp',
        ),
    ]
