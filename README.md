py-tools
========

This repository contains my ptools Python package. This package incorporates various Python modules I have developed.

Contents
--------
- dir_corrs.py - This module contains functions which perform various directory-based correlation analysis, specifically on nifti neuro-imaging data.
- fetch_creds.py - This module contains functions which return sensitive information from a csv file, with regards to connection to AWS services.

Dependencies
------------
- [Boto](http://boto.readthedocs.org/en/latest/) - Python package for interacting with Amazon Web Services
- [cx_Oracle](http://cx-oracle.readthedocs.org/en/latest/index.html) - Python package for interacting with Oracle databases
- [Nibabel](http://nipy.org/nibabel/api.html) - Python package for read/write access to various neuroimaging data formats
- [Numpy](http://docs.scipy.org/doc/numpy/reference/) - Python package for fast numerical computations
- [pandas](http://pandas.pydata.org/) - Python package for providing high-performance and easy-to-use data structures/analysis tools
