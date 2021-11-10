from django.shortcuts import get_object_or_404
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from account.auth import CustomAuthentication
from api.administrator.serializers import PollSerializer, QuestionSerializer
from polls.models import Poll, Question


class PollsViewSet(viewsets.ViewSet):

    authentication_classes = [CustomAuthentication]

    @swagger_auto_schema(responses={200: PollSerializer})
    def list(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: PollSerializer})
    def retrieve(self, request, pk=None):
        queryset = Poll.objects.all()
        poll = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    @swagger_auto_schema(responses={201: PollSerializer}, request_body=PollSerializer)
    def create(self, request):
        serializer = PollSerializer(data=request.data)
        questions = []
        if request.data['question_create_new']:
            for question in request.data['questions']:
                questions.append(Question.objects.create(**question))
        else:
            for question in request.data['questions']:
                questions.append(
                    get_object_or_404(
                        Question.objects.all(), pk=question['id']
                    )
                )
        if serializer.is_valid():
            serializer.save(questions=questions)
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(responses={201: PollSerializer}, request_body=PollSerializer)
    def update(self, request, pk=None):
        queryset = Poll.objects.all()
        poll = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(poll, data=request.data)
        questions = []
        if request.data['question_create_new']:
            for question in request.data['questions']:
                questions.append(Question.objects.create(**question))
        else:
            for question in request.data['questions']:
                questions.append(
                    get_object_or_404(
                        Question.objects.all(), pk=question['id']
                    )
                )
        poll.questions.set(questions)
        if serializer.is_valid():
            serializer.update(poll, request.data)
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(responses={200: PollSerializer})
    def destroy(self, request, pk=None):
        queryset = Poll.objects.all()
        poll = get_object_or_404(queryset, pk=pk)
        data = PollSerializer(poll).data
        poll.delete()
        return Response(data)


class QuestionsViewSet(viewsets.ViewSet):

    authentication_classes = [CustomAuthentication]

    def list(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.update(question, request.data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        data = QuestionSerializer(question).data
        question.delete()
        return Response(data)