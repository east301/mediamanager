import pytest
from django.db import IntegrityError


def verify_model_unique_constraint(generate_item):
    """
    Tests model's unique constraint.

    :param callable generate_item: function to generate ORM object to be tested
    """

    generate_item().save()

    with pytest.raises(IntegrityError):
        generate_item().save()
