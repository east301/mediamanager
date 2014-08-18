import pytest
from django.core.management import color
from django.db import connection, models
from .orm import get_object_or_none


@pytest.mark.django_db
def test__get_object_or_none__returns_correct_result():
    #
    class Meta: pass

    KeyValuePair = type('KeyValuePair', (models.Model,), {
        'key': models.CharField(max_length=128, unique=True),
        'value': models.CharField(max_length=128, unique=True),
        '__module__': 'apps.lib.test_orm',
        'Meta': Meta
    })

    style = color.no_style()
    stmts = connection.creation.sql_create_model(KeyValuePair, style, [])[0]

    cursor = connection.cursor()
    for stmt in stmts:
        cursor.execute(stmt)

    #
    value = get_object_or_none(KeyValuePair, key='foo')
    assert value is None

    #
    KeyValuePair(key='foo', value='bar').save()

    value = get_object_or_none(KeyValuePair, key='foo')
    assert value is not None
    assert value.key == 'foo'
    assert value.value == 'bar'
