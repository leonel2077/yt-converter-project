from django import template

register = template.Library()

@register.filter
def bytes_to_mb(value):
    """Convierte el tamaño en bytes a MB con dos decimales."""
    try:
        mb = float(value) / (1024 * 1024)
        return "{:.2f} MB".format(mb)
    except (ValueError, TypeError):
        return "N/A"
