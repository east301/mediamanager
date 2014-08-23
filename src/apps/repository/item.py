import importlib
import mimetypes
import os
import PIL.Image
from apps.lib.orm import get_object_or_none
from .models import ItemType

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class ItemProcessor(object):
    """Performs several operations on item."""

    def generate_thumbnail(self, path, width, height):
        """
        Generates thumbnail of the specified image.

        :param str path: target item path
        :param int width: thumbnail width
        :param int height: thumbnail height

        :rtype: PIL.Image.Image
        :returns: thumbnail
        """

        raise NotImplementedError  # pragma: no cover


class ImageItemProcessor(ItemProcessor):
    """An implementation of ItemProcessor class for images."""

    def generate_thumbnail(self, path, width, height):
        """{{INHERIT DOC}}"""

        with open(path, 'rb') as fin:
            image = PIL.Image.open(fin).copy()
            image.thumbnail((width, height), PIL.Image.ANTIALIAS)
            return image


def get_item_type_from_path(path):
    """
    Gets ItemType object that corresponds the speicified file.

    :param str path: path to a file

    :rtype: apps.repository.models.ItemType
    :returns: item type of the specified file
    """

    mime_type = mimetypes.guess_type(path)[0]
    if mime_type:
        item_type = get_object_or_none(ItemType, mime_type=mime_type)
        if item_type:
            return item_type

    return None


def generate_thumbnail_of_item(item, width, height, format):
    """
    Generates thumbnail of the specified item.

    :param apps.repository.models.Item: target item
    :param int width: width of thumbnail to be generated
    :param int height: height of thumbnail to be generated
    :param str format: format of thumbnail to be generated

    :rtype: str
    :returns: thumbnail data (byte array)
    """

    #
    pp = item.type.processor
    mod = importlib.import_module(pp[:pp.rindex('.')])
    processor = getattr(mod, pp[pp.rindex('.')+1:])()

    #
    thumb = processor.generate_thumbnail(item.path, width, height)

    #
    buf = StringIO()
    thumb.save(buf, format)

    return buf.getvalue()
