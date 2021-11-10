from rest_framework import serializers
from polls.models import Poll, PollResult, Question, UserAnswer


class AnswerReadSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    user_answer = serializers.CharField()


class PollResultReadSerializer(serializers.Serializer):
    poll_id = serializers.IntegerField()
