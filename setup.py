#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import dingos_authoring

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = dingos_authoring.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-dingos-authoring',
    version=version,
    description="""Support for authoring of data to be imported into Dingos.""",
    long_description=readme + '\n\n' + history,
    author='Siemens',
    author_email='mantis.cert@siemens.com',
    url='https://github.com/siemens/django-dingos-authoring',
    packages=[
        'dingos_authoring',
    ],
    include_package_data=True,
    install_requires=[
        'django-dingos>=0.3.0,<0.4.0',

    ],
    license="GPLv2+",
    zip_safe=False,
    keywords='django-dingos-authoring',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
    ],
)
