import pytest
from django.db import IntegrityError
from apps.lib.test import verify_model_unique_constraint
from .models import Item, ItemGroup, ItemGroupEntry, ItemTag, ItemType


@pytest.mark.django_db
def test__Item__path__unique_constraint():
    type = ItemType.objects.get_or_create(mime_type='image/jpeg', extension='.jpg')[0]
    verify_model_unique_constraint(lambda: Item(path='/foo.jpg', type=type))


@pytest.mark.django_db
def test__ItemType__extension__unique_constraint():
    ItemType(mime_type='image/jpg', extension='.jpg').save()

    with pytest.raises(IntegrityError):
        ItemType(mime_type='image/jpeg', extension='.jpg').save()


@pytest.mark.django_db
def test__ItemType__mime_type__unique_constraint():
    ItemType(mime_type='image/jpeg', extension='.jpg').save()

    with pytest.raises(IntegrityError):
        ItemType(mime_type='image/jpeg', extension='.jpeg').save()


@pytest.mark.django_db
def test__ItemGroupEntry__item_group__item__unique_constraint():
    type = ItemType.objects.get_or_create(mime_type='image/jpeg', extension='.jpg')[0]

    item = Item(path='/foo.jpg', type=type)
    item.save()

    group = ItemGroup()
    group.save()

    verify_model_unique_constraint(lambda: ItemGroupEntry(item_group=group, item=item))


@pytest.mark.django_db
def test__ItemTag__label__unique_constraint():
    verify_model_unique_constraint(lambda: ItemTag(label='foo'))
