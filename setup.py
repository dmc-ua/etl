#!/usr/bin/env python3.5
# coding=utf-8

from pip.req import parse_requirements
from pip.download import PipSession

from setuptools import setup, find_packages

parsed_requirements = parse_requirements(
    'requirements.txt',
    session=PipSession()
)

requirements = [str(ir.req) for ir in parsed_requirements]

setup(
    name='etl',
    version='0.0.11',
    description='ETL CLI tool',
    long_description='Extract transform load CLI tool for extracting small '
                     'and middle data volume from sources (databases, '
                     'csv files, xls files, gspreadsheets) '
                     'to target (databases, csv files, xls files, '
                     'gspreadsheets) in free combination.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='etl',
    entry_points={'console_scripts': ['etl=etl.etl:run_console']},
)
