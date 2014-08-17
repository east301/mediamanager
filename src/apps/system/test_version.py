from .version import get_application_version_hash


def test__get_application_version_hash__returns_correct_result():
    result = get_application_version_hash()
    assert isinstance(result, basestring)
    assert (result in ('(ERROR)', '(UNKNOWN)')) or len(result) == 12
