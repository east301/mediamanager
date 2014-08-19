import os
import pytest
from django.core.management import call_command
from .models import Item, ItemGroup, ItemGroupEntry, ItemTag, ItemType


@pytest.mark.django_db
def test__import_items__with_file_path():
    assert Item.objects.count() == 0

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata', 'images', 'image0.png')
    call_command('import_items', path)

    assert Item.objects.count() == 1
    assert Item.objects.all()[0].path == path


@pytest.mark.django_db
def test__import_items__without_recursive_argument():
    assert Item.objects.count() == 0

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata', 'images')
    call_command('import_items', path)

    assert Item.objects.count() == 1
    assert Item.objects.all()[0].path == os.path.join(path, 'image0.png')


@pytest.mark.django_db
def test__import_items__with_recursive_argument():
    assert Item.objects.count() == 0

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testdata', 'images')
    call_command('import_items', path, recursive=True)

    assert Item.objects.count() == 3

    actual_paths = frozenset(i.path for i in Item.objects.all())
    expected_paths = frozenset([
        os.path.join(path, 'image0.png'),
        os.path.join(path, 'dir', 'image1.png'),
        os.path.join(path, 'dir', 'image2.png'),
    ])
    assert actual_paths == expected_paths
