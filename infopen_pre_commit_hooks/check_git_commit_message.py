"""
Hook to check commit messages
"""
import argparse
import sys


def check_git_commit_message(argv=None):
    """
    Hook entry point
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename', nargs='1', help='Filename containing commit message.',
    )
    args = parser.parse_args(argv)

    retval = 0

    with open(args.filename) as commit_message_file:
        print(commit_message_file.read)

    return retval


if __name__ == '__main__':
    sys.exit(check_git_commit_message())
