# Generated by Django 3.0.5 on 2020-04-23 14:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_auto_20200423_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]