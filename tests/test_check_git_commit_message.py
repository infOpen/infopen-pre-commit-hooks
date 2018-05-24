"""
check_rst precommit testing
"""
import pytest

from infopen_pre_commit_hooks.check_git_commit_message \
    import check_git_commit_message
from testing.util import get_resource_path


@pytest.mark.parametrize(
    'filename,expected_retval', [
        ('bad_commit_line_with_invalid_prefix.txt', 1),
        ('bad_commit_line_with_invalid_size.txt', 1),
        ('bad_commit_line_without_prefix.txt', 1),
        ('bad_commit_line_without_empty_line.txt', 1),
        ('ok_commit_line_with_valid_prefix.txt', 0),
    ],
)
def test_check_git_commit_message(filename, expected_retval):
    """
    Check pre-commit git commit message linter
    """

    argv = [get_resource_path(filename)]
    ret = check_git_commit_message(argv=argv)
    assert ret == expected_retval
