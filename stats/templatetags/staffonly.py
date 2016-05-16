from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def staffonly(context, users):
    r = []
    request = context['request']
    if request.user.is_superuser or request.user.is_staff:
        staff = True
    else:
        staff = False

    for user in users:
        if (user.is_superuser or user.is_staff) and (request.user.is_staff or request.user.is_superuser):
            r.append(user)
        elif (user.is_superuser or user.is_staff) and (not request.user.is_staff and not request.user.is_superuser):
            pass
        else:
            r.append(user)


    return r
