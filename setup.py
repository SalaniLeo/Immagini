from setuptools import setup
from info import __version__
from setuptools import find_packages

setup(
   name='Flake',
   version=__version__,
   author='salaniLeo',
   author_email='leonardo07.salani@gmail.com',
   packages=find_packages("src"),
   url='https://github.com/SalaniLeo/Flake',
   license='GPL-3.0',
   description='GTK user interface for appimagekit Lets you create AppImages with ease',
   long_description=open('README.md').read(),
   install_requires=[

   ],
   
)
