# Generated by Django 3.2.7 on 2021-11-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ImageField(null=True, upload_to='userprofile'),
        ),
    ]