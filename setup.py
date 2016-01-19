#!/usr/bin/env python
#
# setup.py
#
# Author: Daniel Clark, 2014

'''
This is the setup.py installation script to install the pytools package
to the local disk.
'''

# Import packages
from distutils.core import setup

# Use disutils' setup function to install the package
setup(name='py-tools',
      version='0.0.3',
      description='Various Python utilities',
      author='Daniel Clark',
      author_email='danieljclark87@gmail.com',
      url='https://github.com/dclark87/py-tools',
      packages=['pytools'])
