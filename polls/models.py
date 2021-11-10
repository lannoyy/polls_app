from django.db import models
from django.contrib.auth.models import User

QUESTIONS_CHOICES = [
    (1, 'TextAnswer'),
    (2, 'SingleChoiceAnswer'),
    (3, 'MultipleChoiceAnswer'),
]


class Question(models.Model):
    text = models.TextField()
    type = models.IntegerField(choices=QUESTIONS_CHOICES)


class Poll(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    questions = models.ManyToManyField(to=Question, null=True)


class PollResult(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.SET_NULL, null=True)
    user = models.IntegerField(default=0)
    answers = models.ManyToManyField(Question, through='UserAnswer')


class UserAnswer(models.Model):
    poll_result = models.ForeignKey(PollResult, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=200)

