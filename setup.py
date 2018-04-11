from setuptools import find_packages
from setuptools import setup


setup(
    name='infopen_pre_commit_hooks',
    description='Infopen out-of-the-box hooks for pre-commit.',
    url='https://github.com/infOpen/pre-commit-hooks',
    version='0.1.0',

    author='Alexandre Chaussier',
    author_email='a.chaussier@infopen.pro',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'autopep8==1.3.5',
        'flake8==3.5.0',
        'pyyaml==3.12.0',
        'restructuredtext_lint==1.1.3',
        'six==1.11.0',
    ],
    entry_points={
        'console_scripts': [
            'check-rst = infopen_pre_commit_hooks.check_rst:check_rst',
        ],
    },
)
