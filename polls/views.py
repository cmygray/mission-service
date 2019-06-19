import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.models import Poll, Choice
from polls.serializers import PollSerializer, ChoiceSerializer


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        polls = Poll.objects.exclude(starts_at=None)
        serializer = PollSerializer(polls, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        body = json.loads(request.body)
        poll = Poll(
            poll_title=body['poll_title']
        )
        poll.save()
        Choice.objects.bulk_create([
            Choice(poll_id=poll),
            Choice(poll_id=poll),
            Choice(poll_id=poll)
        ])

        serializer = PollSerializer(poll)

        return Response(serializer.data)


@api_view(['GET', 'PATCH'])
def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'GET':
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    if request.method == 'PATCH':
        body = json.loads(request.body)

        poll = Poll.objects.get(pk=poll_id)

        serializer = PollSerializer(poll)
        serializer.update(poll, body)

        return Response(serializer.data)


@api_view(['POST'])
def vote(request, poll_id):
    if request.method == 'POST':
        body = json.loads(request.body)
        choice = Choice.objects.get(pk=body['choice_id'])

        choice_serializer = ChoiceSerializer(choice)
        choice_serializer.increment_votes_count(choice)

        poll = Poll.objects.get(pk=poll_id)
        poll_serializer = PollSerializer(poll)

        return Response(poll_serializer.data)

