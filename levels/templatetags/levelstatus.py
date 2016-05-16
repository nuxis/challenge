from django import template

register = template.Library()

@register.filter
def level_user_status(value, arg):
    return value.get_user_status(arg)
