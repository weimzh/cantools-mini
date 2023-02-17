#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
import re


def find_version():
    return re.search(r"^__version__ = '(.*)'$",
                     open('cantools/version.py', 'r').read(),
                     re.MULTILINE).group(1)


setup(name='cantools_mini',
      version=find_version(),
      description='CAN BUS tools.',
      long_description=open('README.rst', 'r').read(),
      author='Erik Moqvist',
      author_email='erik.moqvist@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      keywords=['can', 'can bus', 'dbc', 'kcd', 'automotive'],
      url='https://github.com/weimzh/cantools-mini',
      packages=find_packages(),
      package_data={"cantools": ["py.typed"]},
      python_requires='>=3.6',
      install_requires=[
          'python-can>=2.2.0',
          'textparser>=0.21.1',
          'argparse_addons',
          'typing_extensions>=3.10.0.0',
      ],
      extras_require=dict(
          plot=['matplotlib'],
      ),
      entry_points = {
          'console_scripts': ['cantools=cantools.__init__:_main']
      })
