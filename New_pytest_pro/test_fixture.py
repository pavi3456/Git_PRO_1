import allure
import pytest


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    a =10
    def finalizer_module_scope_fixture():
        allure.attach('A text attachment in module scope finalizer', 'blah blah blah blah',
                      allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)
    return a


def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    b = 10
    allure.attach('value matched with a: %s and b: %s' % (str(attach_file_in_module_scope_fixture_with_finalizer), b),
                  "first_test_case", allure.attachment_type.TEXT)
    assert int(attach_file_in_module_scope_fixture_with_finalizer) == b
