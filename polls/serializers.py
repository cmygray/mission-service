from rest_framework import serializers
from polls.models import Choice, Poll


class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Choice
        fields = '__all__'

    def increment_votes_count(self, instance):
        instance.votes_count += 1
        instance.save()
        return instance


class PollSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Poll
        fields = '__all__'
        depth = 1

    def update(self, instance, validated_data):
        choices_data = validated_data.pop('choices')
        choices = instance.choices.all()

        for choice_data in choices_data:
            choice = choices.get(id=choice_data.get('id'))
            choice.choice_text = choice_data.get('choice_text', choice.choice_text)
            choice.save()

        instance.poll_title = validated_data.get('poll_title', instance.poll_title)
        instance.starts_at = validated_data.get('starts_at', instance.starts_at)
        instance.ends_at = validated_data.get('ends_at', instance.ends_at)
        instance.save()
        return instance
