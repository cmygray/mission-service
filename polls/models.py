from django.db import models


class Poll(models.Model):
    poll_title = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)


class Choice(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(blank=True, max_length=200, default='항목을 입력하세요')
    votes_count = models.IntegerField(default=0)
