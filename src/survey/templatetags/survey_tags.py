from django import template


register = template.Library()


@register.filter
def remove_underscores(value):
    value = value.replace('_', ' ')
    value = value.replace('and or', 'and/or')
    return value


register.filter('remove_', remove_underscores)
