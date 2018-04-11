"""
Common utils functions
"""
import os.path


TESTING_DIR = os.path.abspath(os.path.dirname(__file__))


def get_resource_path(path):
    """
    Return absolute ressource path
    :param path: Ressource filename
    :type arg1: str
    :return: Absolute resource path
    :rtype: str
    """

    return os.path.join(TESTING_DIR, 'resources', path)
