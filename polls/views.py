import json
from django.core.serializers import serialize
from django.http import HttpResponse

from polls.models import Poll


def index(request):
    if request.method == 'GET':
        return HttpResponse(
            serialize('json', Poll.objects.all()),
            content_type='application/json',
        )


def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'GET':
        return HttpResponse(
            json.loads(serialize('json', [poll])),
            content_type='application/json',
        )
