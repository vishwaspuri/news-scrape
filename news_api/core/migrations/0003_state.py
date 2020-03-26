# Generated by Django 3.0.4 on 2020-03-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_article_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=100)),
                ('india_confirmed_cases', models.IntegerField()),
                ('foreign_confirmed_cases', models.IntegerField()),
                ('cured_cases', models.IntegerField()),
                ('deaths_caused', models.IntegerField()),
            ],
        ),
    ]