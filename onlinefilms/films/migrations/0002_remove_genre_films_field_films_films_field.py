# Generated by Django 4.2.5 on 2023-12-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='films_field',
        ),
        migrations.AddField(
            model_name='films',
            name='films_field',
            field=models.ManyToManyField(to='films.genre'),
        ),
    ]
