# Generated by Django 3.1.7 on 2021-03-07 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210307_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdata',
            name='typ',
            field=models.CharField(default='action', max_length=100),
        ),
    ]
