import os
import pytest
import PIL.Image
from .item import ImageItemProcessor, generate_thumbnail_of_item
from .models import Item, ItemType

try:
    from cStringIO import StringIO
except ImportError:  # pragma: no cover
    from StringIO import StringIO


@pytest.fixture(scope='module')
def images():
    #
    my_dir_path = os.path.dirname(os.path.abspath(__file__))
    test_image_dir_path = os.path.join(my_dir_path, 'testdata', 'images')

    f = lambda *args: os.path.join(test_image_dir_path, *args)
    image_paths = [f('image0.png'), f('dir', 'image1.png'), f('dir', 'image2.png')]

    images = []
    for image_path in image_paths:
        item_type = ItemType.objects.get(mime_type='image/jpeg')
        item = Item(path=image_path, type=item_type)
        item.save()

        images.append(item)

    return images


@pytest.mark.django_db
def test__ImageItemProcessor__generate_thumbnail(images):
    processor = ImageItemProcessor()
    thumb = processor.generate_thumbnail(images[0].path, 180, 160)

    assert thumb is not None
    assert thumb.size[0] <= 180
    assert thumb.size[1] <= 160


@pytest.mark.django_db
def test__generate_thumbnail_of_item__proper_item_processor(monkeypatch, images):
    #
    class ExpectedException(Exception):
        pass

    class TestImageItemProcessor(object):
        def generate_thumbnail(self, *args, **kwargs):
            raise ExpectedException

    monkeypatch.setattr('apps.repository.item.ImageItemProcessor', TestImageItemProcessor)

    #
    with pytest.raises(ExpectedException):
        generate_thumbnail_of_item(images[0], 180, 160, 'png')


@pytest.mark.django_db
def test__generate_thumbnail_of_item__image_size(monkeypatch, images):
    image_data = generate_thumbnail_of_item(images[0], 180, 160, 'png')
    assert image_data is not None

    buf = StringIO(image_data)
    image = PIL.Image.open(buf)

    assert image.format == 'PNG'
    assert image.size[0] < 180
    assert image.size[1] < 160
