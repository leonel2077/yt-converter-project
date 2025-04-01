import re
from django import template

register = template.Library()

@register.filter
def youtube_id(url):
    """Extrae el ID del video de una URL de YouTube."""
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([0-9A-Za-z_-]{11})'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return ''
