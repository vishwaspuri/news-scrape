# Generated by Django 3.0.4 on 2020-03-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='NationalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('number_of_cases', models.IntegerField()),
            ],
        ),
    ]