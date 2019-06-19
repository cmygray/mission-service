from rest_framework import serializers
from polls.models import Choice, Poll


class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Poll
        fields = '__all__'
        depth = 1
