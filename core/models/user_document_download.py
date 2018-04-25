from django.db import models
from core.models.abstract import UserDocumentInteraction

class UserDocumentDownload(UserDocumentInteraction):
    """Tracks how many times a document was downloaded"""
    downloaded_at = models.DateTimeField(auto_now_add=True)
