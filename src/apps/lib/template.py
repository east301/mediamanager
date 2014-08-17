import functools
from django.shortcuts import render


def render_to(template):
    """
    render_to decorator.

    :param str template: path to template file

    :rtype: django.http.HttpResponse
    :returns: rendering result wrapped as HttpResponse
    """

    def decorate_view(view):
        @functools.wraps(view)
        def invoke_view(request, *args, **kwargs):
            result = view(request, *args, **kwargs)
            if (result is not None) and isinstance(result, dict):
                result = render(request, template, result)

            return result

        return invoke_view

    return decorate_view
