# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='Optional exercise - Twitter and Selenium',
    version='0.1.0',
    description='Optional exercise for Verificacion y Desarrollo',
    long_description=readme,
    author='Pablo Ruiz - Miguel Mayoral',
    author_email='pablo.encinas@live.u-tad.com - miguel.mayoral@live.u-tad.com',
    packages=find_packages(exclude=('tests', 'docs'))
)