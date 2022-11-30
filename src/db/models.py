# db/models.py
from django.db import models

MESSAGE_MATCH_ACTIONS = (
    ('delete', 'Delete'),
    ('ban', 'Ban'),
    ('warn', 'Warn'),
    ('mute', 'Mute'),
    ('ignore', 'Ignore'),
)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    language_code = models.CharField(max_length=10, null=True, blank=True)
    is_bot = models.BooleanField(default=False, null=True, blank=True)

class Message(models.Model):
    message_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_id = models.IntegerField(null=True)
    text = models.TextField()
    date = models.DateTimeField()

class BannedWord(models.Model):
    word = models.CharField(max_length=50)
    word_is_regex = models.BooleanField(default=False)
    exact_match_action = models.CharField(
        max_length=50, default='delete', choices=MESSAGE_MATCH_ACTIONS,
    )
    partial_match_action = models.CharField(
        max_length=50, default='ignore', choices=MESSAGE_MATCH_ACTIONS,
    )
    schedule_time = models.IntegerField(default=0)

class Settings(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
