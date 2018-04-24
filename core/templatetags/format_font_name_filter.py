from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def format_font_name(value):
    """Formats a font name into the display version"""
    return value \
        .replace('_', ' ') \
        .title()
