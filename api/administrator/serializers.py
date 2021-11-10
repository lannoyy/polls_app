from rest_framework import serializers

from polls.models import Poll, Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['type', 'text']


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'start_time', 'end_time', 'questions']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance

