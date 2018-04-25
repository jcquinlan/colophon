from django import template

register = template.Library()

@register.filter
def check_if_favorited(document, user):
    """Returns boolean of whether or not a user favorited this document"""
    return document.is_favorited(user)
