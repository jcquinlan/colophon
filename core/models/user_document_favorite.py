from django.db import models
from core.models.abstract import UserDocumentInteraction

class UserDocumentFavorite(UserDocumentInteraction):
    """Tracks which documents a user has favorited"""
    favorited_at = models.DateTimeField(auto_now_add=True)
