# Generated by Django 2.0.2 on 2018-04-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180427_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]