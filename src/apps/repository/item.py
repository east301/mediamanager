import mimetypes
import os
import PIL.Image
from apps.lib.orm import get_object_or_none
from .models import ItemType


class ItemProcessor(object):
    """Performs several operations on item."""

    def generate_thumbnail(self, item, width, height):
        """
        Generates thumbnail of the specified image.

        :param apps.repository.models.Item item: target item
        :param int width: thumbnail width
        :param int height: thumbnail height

        :rtype: PIL.Image.Image
        :returns: thumbnail
        """

        raise NotImplementedError


class ImageItemProcessor(ItemProcessor):
    """An implementation of ItemProcessor class for images."""

    def generate_thumbnail(self, item, width, height):
        """{{INHERIT DOC}}"""

        with open(item.path, 'rb') as fin:
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
