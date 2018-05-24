"""
Hook to check commit messages
"""
import argparse
import re
import sys


def has_valid_summary_prefix(message):
    """
    Check summary line prefixes
    """
    if re.search(r'^(bump version|chg|fix|merge|new) ?[:-] \w+.*', message[0]):
        return True

    print(
        'Invalid commit summary prefix',
        'valid values : (bump version|chg|fix|merge|new)',
    )
    return False


def has_valid_lines_size(message, line_max_size=80):
    """
    Check line size of the commit message
    """
    result = True

    for index, line in enumerate(message, start=1):

        line_size = len(line)

        if index == 2 and line_size != 0:
            print('Second line must be empty')
            result = False

        if line_size > line_max_size:
            print('Line {} too long: {} instead {} chars'.format(
                index, line_size, line_max_size,
            ))
            result = False

    return result


def check_git_commit_message(argv=None):
    """
    Hook entry point
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename', help='Filename containing commit message.',
    )
    args = parser.parse_args(argv)

    message = []

    with open(args.filename) as commit_message_file:
        message = commit_message_file.readlines()

    check_lines_size = has_valid_lines_size(message)
    check_summary_prefix = has_valid_summary_prefix(message)

    if check_lines_size and check_summary_prefix:
        return 0

    return 1


if __name__ == '__main__':
    sys.exit(check_git_commit_message())
