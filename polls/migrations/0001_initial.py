# Generated by Django 2.2.10 on 2021-11-08 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(editable=False)),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PollResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'TextAnswer'), (2, 'SingleChoiceAnswer'), (3, 'MultipleChoiceAnswer')])),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(max_length=200)),
                ('is_right_answer', models.BooleanField()),
                ('poll_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.PollResult')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
        migrations.AddField(
            model_name='pollresult',
            name='answers',
            field=models.ManyToManyField(through='polls.UserAnswer', to='polls.Question'),
        ),
        migrations.AddField(
            model_name='pollresult',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.Poll'),
        ),
        migrations.AddField(
            model_name='pollresult',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poll',
            name='questions',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]
