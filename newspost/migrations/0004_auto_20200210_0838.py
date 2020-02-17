# Generated by Django 3.0.2 on 2020-02-10 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspost', '0003_auto_20200209_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='main_news',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slider',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
