# Generated by Django 4.1.7 on 2023-03-31 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_rename_movie_movies_rename_user_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='First_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='Last_name',
        ),
    ]
