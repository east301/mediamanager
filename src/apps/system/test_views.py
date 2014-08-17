import pytest
from .views import base, version


def test__base__returns_correct_response(rf):
    response = base(rf.get('/'))
    assert response.status_code == 200
    assert 'hello world' in response.content.lower()


def test__version__returns_correct_response(rf):
    response = version(rf.get('/'))
    assert response.status_code == 200
    assert response['Content-Type'] == 'text/plain'
