from django.db import models


class Poll(models.Model):
    poll_title = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField(blank=False)
    ends_at = models.DateTimeField(blank=False)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes_count = models.IntegerField(default=0)
