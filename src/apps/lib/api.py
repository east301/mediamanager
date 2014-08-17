import functools
import json
from django.http import HttpResponse


class APIError(Exception):
    """
    Represents an error while processing API request.
    """

    def __init__(self, code, messages):
        """
        Initializes an instance of APIError class.

        :param int code: status code
        :param list[str] messages: error messages
        """

        self.code = code
        self.messages = messages


def api(params_validator_cls=None, get_params_from_request=lambda r: r.GET):
    """
    Wraps the specified view as an API view.

    :params django.forms.Form params_validator_cls: API parameter validator
    :params callable get_params_from_request: a function to get API parameters from request object

    :rtype: django.http.HttpResponse
    :returns: an instance of HttpResponse class which contains API response
    """

    def decorate_view(view):
        @functools.wraps(view)
        def invoke_view(request, *args, **kwargs):
            return _invoke_api_view_and_render_response(
                params_validator_cls, get_params_from_request, view, request, *args, **kwargs)

        return invoke_view

    return decorate_view


get_api = lambda v=None: api(v, lambda r: r.GET)
post_api = lambda v=None: api(v, lambda r: r.POST)


def _invoke_api_view_and_render_response(
        params_validator_cls, get_params_from_request, view, request, *args, **kwargs):

    #
    try:
        params = _validate_api_parameters(params_validator_cls, get_params_from_request, request)
        response_data = view(request, params, *args, **kwargs)
        if isinstance(response_data, HttpResponse):
            return response_data

        status_code = 200
        response = dict(status='OK', response=response_data)

    except APIError, ex:
        status_code = ex.code
        response = dict(status='ERROR', error=dict(code=ex.code, messages=ex.messages))

    except:
        status_code = 500
        response = dict(status='ERROR', error=dict(code=500, messages=['Unknown error happened.']))

    #
    response = json.dumps(response, indent=2)
    return HttpResponse(response, content_type='application/json', status=status_code)


def _validate_api_parameters(validator_cls, get_params_from_request, request):
    #
    if not validator_cls:
        return dict()

    #
    validator = validator_cls(get_params_from_request(request))
    if validator.is_valid():
        return validator.cleaned_data
    else:
        errors = ['Invalid value specified as `{}`.'.format(f) for f in validator.errors]
        raise APIError(400, errors)
