# Generated by Django 2.2.10 on 2021-11-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211109_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='questions',
            field=models.ManyToManyField(null=True, to='polls.Question'),
        ),
    ]
