# Generated by Django 3.0.2 on 2020-02-03 06:22

from django.db import migrations, models
import django.db.models.deletion
import newspost.models


class Migration(migrations.Migration):

    dependencies = [
        ('newspost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[newspost.models.customLengthValidator, newspost.models.atValidator])),
                ('description', models.TextField(blank=True, null=True)),
                ('view_count', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspost.Category')),
            ],
        ),
    ]