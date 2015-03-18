# dir_corrs.py
#
# Author: Daniel Clark, 2014

'''
This module contains functions which perform various directory-based 
correlation analysis.
'''


# Plot a dictionary of 
def barplot_dict(in_dict):
    '''
    Method to read in a dictionary of label-number key-value pairs and
    plot a bar graph, with a bar for each dictionary element

    Parameters
    ----------
    dir1 : dictionary (string:number)
        A dictionary with the label for the statistic as an element's
        key and its numeric value as an element's value
        value
    Returns
    -------

    '''

    # Import packages
    import matplotlib.pyplot as plt

    # Setup plot
    plt.bar(range(len(in_dict)), in_dict.values(), align='center')
    plt.xticks(range(len(in_dict)), in_dict.keys())

    # Show plot
    plt.show()


# Calculate correlations between directory-matching nifti files
def nifti_corrs(dir1, dir2, filt_str=''):
    '''
    Method to read all of the nifti files within two paths and
    calculate the correlation between files with matching dirs/names

    Parameters
    ----------
    dir1 : string (directory)
        path to the root directory of the first comparison folder
    dir2 : string (directory)
        path to the root directory of the second comparison folder
    filt_str : string, optional
        setting this argument will filter the found filepaths to
        return the files only with filt_str in its name
    Returns
    -------
    corr_dict : dictionary
        A dictionary with the filepath as the key and the correlation
        as the value
    dir1_only : list (str)
        A list of the files that were only found in dir1 and not dir2, 
        as such, no correlations were computed for these
    dir2_only : list (str)
        A list of the files that were only found in dir2 and not dir1, 
        as such, no correlations were computed for these
    '''

    # Import packages
    import nibabel as nb
    import numpy as np
    import os

    # Init variables
    dir1_niftis = []
    dir2_niftis = []
    dir1_only = []
    dir2_only = []
    corr_dict = {}

    # Walk through each directory to create lists of nifti paths
    print 'Walking through %s...' % dir1
    for root, dirs, files in os.walk(dir1):
        fp = [root + '/' + f for f in files if f.endswith('.nii.gz') and \
                (filt_str in root or filt_str in f)]
        dir1_niftis.extend(fp)
    print 'Walking through %s...' % dir2
    for root, dirs, files in os.walk(dir2):
        fp = [root + '/' + f for f in files if f.endswith('.nii.gz') and \
                (filt_str in root or filt_str in f)]
        dir2_niftis.extend(fp)

    # Create relative directory lists
    rel_dir1_niftis = [f.split(dir1)[1] for f in dir1_niftis]
    rel_dir2_niftis = [f.split(dir2)[1] for f in dir2_niftis]
    no_files = len(rel_dir1_niftis)
    # Iterate through the first path and grab items from the second
    print '\nDone creating correlation lists, now computing correlations on %d files:\n' % no_files
    i = 0
    for f in rel_dir1_niftis:
        # If the file is also in dir2, do correlation
        if f in rel_dir2_niftis:
            # Update progress to stdout
            per = 100*(float(i)/no_files)
            print 'Correlating: %s\nFile no: %d/%d\n%f%% complete' % (f, i, no_files, per)
            file1 = os.path.abspath(dir1 + f)
            file2 = os.path.abspath(dir2 + f)
            f1_exists = os.path.exists(file1)
            f2_exists = os.path.exists(file2)
            # Check if the inputs exist
            if not (f1_exists and f2_exists):
                err = 'One of the input files is missing or not correct'
                err = err + '\n%s exists: %d\n%s exists: %d' \
                            % (file1, f1_exists, file2, f2_exists)
            img1 = nb.load(file1).get_data()
            img2 = nb.load(file2).get_data()
            arr1 = img1.flatten()
            arr2 = img2.flatten()
            # Test to see if the arrays are the same length
            if len(arr1) != len(arr2):
                err = 'The input arrays must be the same length'
                err = err + '\n%s has %d elements, %s has %d elements' \
                             % (dir1+f, len(arr1), dir2+f, len(arr2))
                raise ValueError, err
            R = np.corrcoef(arr1,arr2)
            rval = R[0,1]
            corr_dict[f] = rval
            print 'Correlation: %f' % rval
        # Otherwise, append it to dir1_only list
        else:
            dir1_only.append(f)
        # Increment file counter
        i += 1

    print '\nDone correlating! Checking for missing/mismatched files between directories...'
    # Check for any extra files in dir2
    for f in rel_dir2_niftis:
        if f not in rel_dir1_niftis:
            dir2_only.append(f)

    print '\nFinished!\n'
    # Print results
    print 'Files that are only in %s: ' % dir1
    print dir1_only
    print 'Files that are only in %s: ' % dir2
    print dir2_only
    print 'Correlation dictionary: '
    print corr_dict

    # Return dictionary
    return corr_dict, dir1_only, dir2_only