# Generated by Django 4.2 on 2023-04-15 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waste_sorting', '0008_post_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='post',
        ),
        migrations.RemoveField(
            model_name='report',
            name='reported_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
