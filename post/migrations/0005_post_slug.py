# Generated by Django 3.2.7 on 2021-11-14 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_rename_author_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
