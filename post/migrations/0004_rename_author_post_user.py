# Generated by Django 3.2.7 on 2021-11-11 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]