import re
from setuptools import find_packages, setup
import sys


def _read_long_description():
    try:
        with open('readme.rst') as fd:
            return fd.read()
    except Exception:
        return None


with open('pakage/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

##with open('requirements/base.txt', 'r') as fd:
##    requirements = fd.read().strip().split('\n')
#
try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name='PythonSemVer',
    version=version,
    url='https://github.com/AAMLLe/PythonSemVer',
    author='AAMLLe',
    author_email='myanh@moneylover.me',
    description='Demo SemVer for Python Project',
    long_description=_read_long_description(),
    packages=find_packages(exclude='test'),
    license='MIT',
#    install_requires=requirements,
    entry_points='''
        [console_scripts]
        semantic-release=semantic_release.cli:main
    ''',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6.3',
    ]
)

