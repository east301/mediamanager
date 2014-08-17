import json
from django import forms
from django.http import HttpResponse
from .api import APIError, api


def test__APIError__check_constructor_and_properties():
    error = APIError(500, ['message1', 'message2'])
    assert error.code == 500
    assert len(error.messages) == 2
    assert error.messages[0] == 'message1'
    assert error.messages[1] == 'message2'


def test__api__no_api_parameter(rf):
    @api(None, None)
    def view(request, params, *args, **kwargs):
        return dict(message='hello world')

    response = view(rf.get('/'))
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/json'

    data = json.loads(response.content)
    assert data['status'] == 'OK'
    assert data['response']['message'] == 'hello world'


def test__api__with_api_parameters_and_valid_parameters(rf):
    class APIParams(forms.Form):
        id = forms.IntegerField()

    @api(APIParams, lambda r: r.GET)
    def view(request, params, *args, **kwargs):
        assert params['id'] == 1
        return dict(message='hello world')

    response = view(rf.get('/?id=1'))
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/json'

    data = json.loads(response.content)
    assert data['status'] == 'OK'
    assert data['response']['message'] == 'hello world'


def test__api__with_api_parameters_and_invalid_parameters(rf):
    class APIParams(forms.Form):
        id = forms.IntegerField()

    @api(APIParams, lambda r: r.GET)
    def view(request, params, *args, **kwargs):
        return dict()  # pragma: no cover

    response = view(rf.get('/?id=foo'))
    assert response.status_code == 400
    assert response['Content-Type'] == 'application/json'

    data = json.loads(response.content)
    assert data['status'] == 'ERROR'
    assert data['error']['code'] == 400
    assert data['error']['messages'][0] == 'Invalid value specified as `id`.'


def test__api__returns_same_httpresponse_instance(rf):
    response0 = HttpResponse('hello world', content_type='text/plain')

    @api(None, None)
    def view(request, params, *args, **kwargs):
        return response0

    response = view(rf.get('/'))
    assert response.status_code == 200
    assert response['Content-Type'] == 'text/plain'
    assert response.content == 'hello world'
    assert response is response0


def test__api__view_raises_an_exception(rf):
    @api(None, None)
    def view(request, params, *args, **kwargs):
        raise Exception

    response = view(rf.get('/'))
    assert response.status_code == 500
    assert response['Content-Type'] == 'application/json'

    data = json.loads(response.content)
    assert data['status'] == 'ERROR'
    assert data['error']['code'] == 500
    assert data['error']['messages'][0] == 'Unknown error happened.'
