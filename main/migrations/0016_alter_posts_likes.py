# Generated by Django 4.0.3 on 2022-04-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_posts_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]