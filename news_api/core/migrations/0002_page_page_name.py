# Generated by Django 3.0.4 on 2020-03-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]