# Generated by Django 4.1 on 2022-09-05 23:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('summary', models.TextField(help_text='Pon aqui la descripcion de la pelicula', max_length=100)),
                ('premier', models.PositiveBigIntegerField()),
                ('runtime', models.PositiveBigIntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cine.author')),
                ('genre', models.ManyToManyField(to='cine.genre')),
            ],
        ),
        migrations.CreateModel(
            name='MovieInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID unico para esta pelicula', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('e', 'Maintenance'), ('o', 'On load'), ('a', 'Available'), ('r', 'Reservado')], default='m', help_text='Disponibilidad de la pelicula', max_length=1)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cine.movie')),
            ],
        ),
    ]