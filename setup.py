# from https://github.com/bast/somepackage/blob/master/setup.py
from setuptools import setup, find_packages

import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'grid', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='somepackage',
    version=version['__version__'],
    description=('Simple python grid'),
    long_description=long_description,
    author='Yoieh',
    author_email='yoieh@live.se',
    url='https://github.com/yoieh/grid',
    packages=find_packages("src"),
    package_dir={"": "src"},
    license="MIT",
    install_requires=_here.joinpath("requirements.txt").read_text().split(
        "\n"),
)
