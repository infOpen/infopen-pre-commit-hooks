import argparse
import sys

import restructuredtext_lint


def check_rst(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='RST filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        errors = restructuredtext_lint.lint_file(filename)
        if errors:
            print('{}: Failed to xml parse ({})'.format(filename, errors))
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_rst())
