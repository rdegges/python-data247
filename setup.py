from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'data247',
    version = '0.1',
    py_modules = ('data247',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['requests>=0.14.2'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/python-data247',
    keywords = 'python data247',
    description = 'An API client for Data 24-7.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
