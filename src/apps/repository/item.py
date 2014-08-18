import mimetypes
import os
from apps.lib.orm import get_object_or_none
from .models import ItemType


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
