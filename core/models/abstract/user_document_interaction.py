from django.db import models
from django.contrib.auth.models import User

class UserDocumentInteraction(models.Model):
    """Tracks an instance of a document being downloaded"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design_document = models.ForeignKey('core.DesignDocument', on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
