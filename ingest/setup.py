# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Ingest',
    version='0.1.0',
    description='Tool to ingest scraped travel risk data to a database.',
    long_description=readme,
    author='Clyde Smets',
    author_email='clyde.smets@gmail.com',
    url='',
    license=license,
    packages=find_packages()
)
