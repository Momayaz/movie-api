# Generated by Django 3.1.7 on 2021-03-07 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviesdata_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviesdata',
            name='image',
        ),
        migrations.AddField(
            model_name='moviesdata',
            name='typ',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
