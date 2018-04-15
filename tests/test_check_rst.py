"""
check_rst precommit testing
"""
import pytest

from infopen_pre_commit_hooks.check_rst import check_rst
from testing.util import get_resource_path


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('bad_rst.rst', 1),
        ('ok_rst.rst', 0),
    ),
)
def test_check_rst(filename, expected_retval):
    """
    Check pre-commit RST linter
    """

    ret = check_rst([get_resource_path(filename)])
    assert ret == expected_retval
