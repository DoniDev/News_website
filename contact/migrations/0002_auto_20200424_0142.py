# Generated by Django 3.0.5 on 2020-04-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='website',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=254),
        ),
    ]
