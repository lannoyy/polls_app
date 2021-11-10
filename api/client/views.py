from typing import List

from django.shortcuts import get_object_or_404
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from api.administrator.serializers import PollSerializer
from api.client.serializers import AnswerReadSerializer, PollResultReadSerializer
from polls.models import Poll, Question, UserAnswer, PollResult


class UsersAnswers(APIView):

    @swagger_auto_schema(responses={200: AnswerReadSerializer})
    def get(self, request, poll_pk=None, user_pk=None):
        queryset_poll = PollResult.objects.all()
        poll = get_object_or_404(queryset_poll, poll=poll_pk, user=user_pk)
        queryset_answer = UserAnswer.objects.filter(
            poll_result=poll
        )
        answer_serializer = AnswerReadSerializer(queryset_answer, many=True)
        return Response(answer_serializer.data)

    @swagger_auto_schema(responses={201: AnswerReadSerializer}, request_body=AnswerReadSerializer)
    def post(self, request, poll_pk=None, user_pk=None):
        answer_serializer = AnswerReadSerializer(request.data, many=True)
        queryset_poll = Poll.objects.all()
        poll = get_object_or_404(queryset_poll, pk=poll_pk)
        poll_result = PollResult.objects.create(
            poll=poll,
            user=user_pk
        )
        for answer in answer_serializer.data:
            question = Question.objects.get(pk=answer['question_id'])
            UserAnswer.objects.create(
                poll_result=poll_result,
                question=question,
                user_answer=answer['user_answer'],
            )
        return Response(answer_serializer.data)


class CompletePolls(APIView):

    @swagger_auto_schema(responses={200: PollResultReadSerializer})
    def get(self, request, user_pk=None):
        polls = PollResult.objects.filter(user=user_pk)
        serializer = PollResultReadSerializer(polls, many=True)
        return Response(serializer.data)


class ActivePolls(APIView):

    @swagger_auto_schema(responses={200: PollSerializer})
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class PollInfo(APIView):

    @swagger_auto_schema(responses={200: PollSerializer})
    def get(self, request, poll_pk=None):
        poll = Poll.objects.get(pk=poll_pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)
