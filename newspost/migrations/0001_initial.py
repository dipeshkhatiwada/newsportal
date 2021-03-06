# Generated by Django 3.0.2 on 2020-02-03 05:37

from django.db import migrations, models
import newspost.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, validators=[newspost.models.customLengthValidator, newspost.models.atValidator])),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[newspost.models.customLengthValidator, newspost.models.atValidator])),
            ],
        ),
    ]
