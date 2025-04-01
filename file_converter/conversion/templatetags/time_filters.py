from django import template

register = template.Library()

@register.filter
def secs_to_mins(seconds):
    """Convierte la duración en segundos a un formato de tiempo.
    Si la duración es menor a una hora, muestra 'mm:ss',
    de lo contrario, muestra 'h:mm:ss'."""
    try:
        seconds = int(seconds)
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            return f"{hour:d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"
    except (ValueError, TypeError):
        return "N/A"
