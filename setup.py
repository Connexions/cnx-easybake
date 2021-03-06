# -*- coding: utf-8 -*-
"""
Copyright (C) 2016 Rice University.

This software is subject to the provisions of the
GNU AFFERO GENERAL PUBLIC LICENSE Version 3.0 (AGPL).
See LICENSE.txt for details.
"""
import os

from setuptools import setup, find_packages
import versioneer


here = os.path.abspath(os.path.dirname(__file__))


def read_from_requirements_txt(filepath):
    f = os.path.join(here, filepath)
    with open(f) as fb:
        return tuple([x.strip() for x in fb if not x.strip().startswith('#')])


install_requires = read_from_requirements_txt('requirements/main.txt')
tests_require = read_from_requirements_txt('requirements/test.txt')
extras_require = {
    'test': tests_require,
}


setup(
    name='cnx-easybake',
    version=versioneer.get_version(),
    author='Connexions team',
    author_email='info@cnx.org',
    url="https://github.com/connexions/cnx-easybake",
    license='LGPL, See also LICENSE.txt',
    description='',
    packages=find_packages(),
    tests_require=tests_require,
    test_suite='cnxeasybake.tests',
    install_requires=install_requires,
    include_package_data=True,
    cmdclass=versioneer.get_cmdclass(),
    entry_points={
        'console_scripts': [
            'cnx-easybake = cnxeasybake.scripts.main:main',
            ],
        },
   )
