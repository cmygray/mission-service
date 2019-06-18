import json
from django.core.serializers import serialize
from django.http import HttpResponse

from polls.models import Poll, Choice


def index(request):
    if request.method == 'GET':
        return HttpResponse(
            serialize('json', Poll.objects.all()),
            content_type='application/json',
        )

    if request.method == 'POST':
        poll = Poll(
            poll_title=request.POST.get('poll_title'),
        )
        poll.save()
        Choice.objects.bulk_create([
            Choice(poll_id=poll.pk),
            Choice(poll_id=poll.pk),
            Choice(poll_id=poll.pk)
        ])
        return HttpResponse(
            json.loads(serialize('json', [poll])),
            content_type='application/json',
        )


def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'GET':
        return HttpResponse(
            json.loads(serialize('json', [poll])),
            content_type='application/json',
        )


def choices(request, poll_id):
    if request.method == 'GET':
        return HttpResponse(
            serialize('json', Poll.objects.get(pk=poll_id).choices.all()),
            content_type='application/json',
        )
