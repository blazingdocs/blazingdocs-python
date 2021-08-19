#!/usr/bin/env python

from setuptools.depends import get_module_constant
from setuptools import setup

setup(
    name='BlazingDocs',
    packages=['blazingdocs'],
    version=get_module_constant('blazingdocs', '__version__'),
    description='BlazingDocs Python client',
    long_description='High-performance document generation API. Generate documents and reports from СSV, JSON, XML with 99,9% uptime and 24/7 monitoring.',
    author='Mentalstack',
    author_email='hello@blazingdocs.com',
    url='https://blazingdocs.com',
    download_url='https://github.com/blazingdocs/blazingdocs-python',
    keywords=['doc', 'docx', 'pdf', 'odt', 'report', 'document', 'template', 'office', 'openoffice', 'merge', 'xml', 'json', 'csv'],
    install_requires=['requests>=2.26.0'],
    classifiers=[],
    license='MIT'
)
