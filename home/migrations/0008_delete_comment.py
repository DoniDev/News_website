# Generated by Django 3.0.5 on 2020-04-20 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_comment_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
