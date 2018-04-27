from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True, blank=True)
    personal_website = models.URLField(null=True, blank=True)
