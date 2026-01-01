from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def staffonly(context, users):
    r = []
    request = context["request"]

    # FIXME: Not sure if this staff= is needed, but will need testing to be sure. noqa'd for now
    if request.user.is_superuser or request.user.is_staff:
        staff = True  # noqa: F841
    else:
        staff = False  # noqa: F841

    for user in users:
        if (user.user.is_superuser or user.user.is_staff) and (
            request.user.is_staff or request.user.is_superuser
        ):
            r.append(user)
        elif (user.user.is_superuser or user.user.is_staff) and (
            not request.user.is_staff and not request.user.is_superuser
        ):
            pass
        else:
            r.append(user)

    return r
