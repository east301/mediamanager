import PIL.Image
import pytest
from django.http import Http404
from .views import image, recent, thumbnail

try:
    from cStringIO import StringIO
except ImportError:  # pragma: no cover
    from StringIO import StringIO


@pytest.fixture
def items():
    import os
    from django.core.management import call_command

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata', 'images')
    call_command('import_items', path)


@pytest.mark.django_db
def test__recent__status_code(rf):
    response = recent(rf.get('/'))
    assert response.status_code == 200


@pytest.mark.django_db
def test__image__invalid_item_id(rf):
    with pytest.raises(Http404):
        image(rf.get('/'), '1')


@pytest.mark.django_db
def test__image__response(rf, items):
    response = image(rf.get('/'), '1')
    assert response.status_code == 200
    assert response['Content-Type'] == 'image/png'

    img = PIL.Image.open(StringIO(response.content))
    assert img.format == 'PNG'
    assert 0 < img.size[0]
    assert 0 < img.size[1]


@pytest.mark.django_db
def test__thumbnail__invalid_item_id(rf):
    with pytest.raises(Http404):
        thumbnail(rf.get('/'), '1')


@pytest.mark.django_db
def test__thumbnail__response(rf, items):
    response = thumbnail(rf.get('/'), '1')
    assert response.status_code == 200
    assert response['Content-Type'] == 'image/png'

    image = PIL.Image.open(StringIO(response.content))
    assert image.format == 'PNG'
    assert 0 < image.size[0] <= 180
    assert 0 < image.size[1] <= 160
