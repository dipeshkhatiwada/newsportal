# Generated by Django 3.0.2 on 2020-02-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspost', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='menu_display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
