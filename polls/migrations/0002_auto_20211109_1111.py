# Generated by Django 2.2.10 on 2021-11-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='start_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pollresult',
            name='user',
            field=models.IntegerField(default=0),
        ),
    ]
