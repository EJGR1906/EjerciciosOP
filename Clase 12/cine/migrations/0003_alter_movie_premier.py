# Generated by Django 4.1 on 2022-09-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0002_author_movie_movieinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='premier',
            field=models.DateField(blank=True, null=True),
        ),
    ]