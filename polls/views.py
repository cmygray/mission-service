import json
from django.core.serializers import serialize
from django.http import HttpResponse
from django.utils.dateparse import parse_datetime

from polls.models import Poll


def index(request):
    if request.method == 'GET':
        return HttpResponse(
            serialize('json', Poll.objects.all()),
            content_type='application/json',
        )

    if request.method == 'POST':
        poll = Poll(
            poll_title=request.POST.get('poll_title'),
            ends_at=parse_datetime(request.POST.get('ends_at')),
        )
        poll.save()
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
