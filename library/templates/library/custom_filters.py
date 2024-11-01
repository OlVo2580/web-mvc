from django import template

register = template.Library()

@register.filter
def get_status(statuses, key):
    return statuses.get(key, 'Unknown')
