from django.contrib.auth.models import User
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='groups')

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_messages', blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    notification_preferences = models.JSONField(default=dict)