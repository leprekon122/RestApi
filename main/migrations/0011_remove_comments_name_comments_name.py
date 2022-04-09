# Generated by Django 4.0.3 on 2022-04-09 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_comments_name_comments_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='name',
        ),
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.posts'),
        ),
    ]