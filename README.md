py-tools
========

This repository contains the Python package pytools. The package contains modules with various useful tools.

Contents
--------
- aws_utils.py - This module contains functions which assist in interacting with AWS services, including uploading/downloading data and file checking.
- dir_corrs.py - This module contains functions which perform various directory-based correlation analysis, specifically on nifti neuro-imaging data.
- fetch_creds.py - This module contains functions which return sensitive information from a csv file, with regards to connection to AWS services.
- file_utils.py - This module contains functions which perform various local file manipulation.
- log_tools.py - This module contains functions which help set up logging for python coding and scripts.

Dependencies
------------
- [Boto](http://boto.readthedocs.org/en/latest/) - Python package for interacting with Amazon Web Services
- [cx_Oracle](http://cx-oracle.readthedocs.org/en/latest/index.html) - Python package for interacting with Oracle databases
- [Nibabel](http://nipy.org/nibabel/api.html) - Python package for read/write access to various neuroimaging data formats
- [Numpy](http://docs.scipy.org/doc/numpy/reference/) - Python package for fast numerical computations
- [SQLAlchemy](http://www.sqlalchemy.org/) - Python SQL toolkit
