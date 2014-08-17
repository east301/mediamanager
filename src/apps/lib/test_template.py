from django.http import HttpResponse
from .template import render_to


def test__render_to__returns_correct_rendering_result(rf):
    @render_to('render_to_test.html')
    def view(request):
        return dict(message='hello world')

    response = view(rf.get('/'))
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.content.strip() == 'message: hello world'


def test__render_to__returns_same_httpresponse_instance(rf):
    response0 = HttpResponse('hello world')

    @render_to('render_to_test.html')
    def view(request):
        return response0

    response = view(rf.get('/'))
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.content.strip() == 'hello world'
    assert response is response0
