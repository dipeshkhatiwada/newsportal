# Generated by Django 3.0.2 on 2020-02-11 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='advertisement/')),
                ('view_count', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'advertisement',
            },
        ),
    ]
