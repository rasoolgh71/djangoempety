import os
import sys
from setuptools import find_packages, setup
with open(os.path.join(os.path.dirname(__file__),'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='django-persion',
    version='1.0',
    package=find_packages(),
    includ_package_data=True,
    licence='BSD license',
    description ='the learn django for example.',
    long_description=README,
    url='',
    author='rasool ghanna',
    author_email='rasool@gamil.com',
    packages=find_packages(),
    #package_data=find_package_data("graphos", only_in_packages=False),
    classifires=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',

    ],

)

