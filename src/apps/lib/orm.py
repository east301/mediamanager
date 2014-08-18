
def get_object_or_none(cls, **kwargs):
    """
    Gets a object which satisfies the specified condition, otherwise returns None.

    :param type cls: model class
    :param dict kwargs: search query

    :rtype:
    :returns:
    """

    try:
        return cls.objects.get(**kwargs)
    except cls.DoesNotExist:
        return None
