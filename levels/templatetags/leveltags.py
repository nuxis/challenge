from django import template

register = template.Library()


@register.simple_tag()
def level_color(level, user):
    return level.level_color(user)


@register.simple_tag()
def level_status(level, user):
    return level.get_user_status(user)
