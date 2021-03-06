# Generated by Django 3.0.2 on 2020-05-07 05:51

from django.db import migrations, models
import newspost.models


class Migration(migrations.Migration):

    dependencies = [
        ('newspost', '0005_category_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, validators=[newspost.models.customLengthValidator, newspost.models.atValidator])),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[newspost.models.customLengthValidator, newspost.models.atValidator])),
                ('rank', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
