# Generated by Django 4.0.3 on 2022-04-27 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_comments_name_comments_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
