"""
kepython
------------
Python utils by kerol, including web and other utils.
Flask is Fun
````````````

Save in a hello.py:

.. code:: python

    from kepython.flask import *

"""

from setuptools import setup
from os import path

#here = path.abspath(path.dirname(__file__))
#with open(path.join(here, 'README.md')) as f:
#        long_description = f.read()

setup(
    name='kepython',
    version='0.1.4',
    description='Python utils by kerol',
    #long_description=long_description,
    url='https://github.com/kerol/kepython',
    author='Kerol Gao',
    author_email='ikerol@163.com',
    license='Apache',
    packages=['kepython',],
    include_package_data=True,
    install_requires=[
        'flask>=0.12',
        'scrapy>=1.3.0',
    ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'kepython=kepython:main',
        ],
    },
)

