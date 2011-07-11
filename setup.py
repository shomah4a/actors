#-*- coding:utf-8 -*-

import setuptools

from scalalike.actors import __version__, __author__, __doc__, __license__



setuptools.setup(
    name='scalalike.actors',
    version=__version__,
    author=__author__,
    author_email='shoma.h4a+pypi@gmail.com',
    license=__license__,
    url='https://github.com/shomah4a/actors',
    description='scala like actor interface for python.',
    long_description=__doc__,
    packages=['scalalike.actors'],
    install_requires=[
        'setuptools',
        ],
    include_dirs=['test', 'test/*.py'],
    namespace_packages=['scalalike'],
    data_files=[
        ('test', ['test/*.py']),
        ],
    include=['test/*.py'],
    classifiers='''
Programming Language :: Python
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Utilities
'''.strip().splitlines())

