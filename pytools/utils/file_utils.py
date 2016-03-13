# file_utils.py
#
# Author: Daniel Clark, 2014

'''
This module has various utilities for handling file manipulation
'''

# Function to compress files in a directory
def compress_files(base_dir, max_size, output_prefix):
    '''
    Function that compresses every single file in a directory in to
    g-zip'd tar files of a specified max size per tar file

    Parameters
    ----------
    base_dir : string
        filepath to the base directory to gather files from for
        compression
    max_size : int
        maximum tar file size (in MB)
    output_prefix : string
        the output filepath to save the tar file to; this string will
        be appended with a '_<no>.tar.gz', where <no> corresponds to
        the number of the tar file created (starting at 0)

    Returns
    -------
    fp_list : list [tuple]
        list of (filepath (str), size (float)) of the found filepaths
    missing: list [str]
        list of missing filepaths that weren't able to compress
    '''

    # Import packages
    import os
    import tarfile

    # Init variables
    fp_list = []

    # Collect files and filesizes
    for root, dirs, files in os.walk(base_dir):
        if files:
            fp_list.extend([(os.path.join(root, f), \
                             os.path.getsize(os.path.join(root, f))/1024.**2) \
                            for f in files])

    # Loop through and create the tar files
    tno = 0
    i = 0
    len_fp = len(fp_list)
    cur_size = 0
    tar = tarfile.open(output_prefix + '_%d.tar.gz' % tno, 'w:gz')
    missing = []

    # For every file in the filepath list
    for fp_size in fp_list:
        fp = fp_size[0]
        size = fp_size[1]
        # If the current size exceeds max, start new tar file
        if cur_size > max_size:
            tar.close()
            tno += 1
            cur_size = 0
            tar = tarfile.open(output_prefix + '_%d.tar.gz' % tno, 'w:gz')
        # Add the file to the tarfile if it exists
        if os.path.exists(fp):
            tar.add(fp)
            cur_size += size
            print 'adding %s to %s, file is %f MB in size' \
                % (fp, tar.name, cur_size)
        # Otherwise, add it to the missing list
        else:
            print 'file %s no longer exists, adding it to missing list'
            missing.append(fp)
        # Increment counter and update percentage complete
        i += 1
        print_loop_status(i, len_fp)

    # Return the file path list and missing
    return fp_list, missing


# Gather files from base directory
def gather_files(base_dir):
    '''
    Function to gather all of the files within a base directory and
    return their filepaths in a list

    Parameters
    ----------
    base_dir : string
        filepath to the base directory where all of the files are
        located

    Returns
    -------
    fp_list : list [str]
        a list of the filepaths
    '''

    # Import packages
    import os

    # Init variables
    fp_list = []

    # Collect files and filesizes
    for root, dirs, files in os.walk(base_dir):
        if files:
            fp_list.extend([os.path.join(root, f) for f in files])

    # Return filepath list
    return fp_list


# Compare m5 sums between two directories
def gather_md5sums(base_dir):
    '''
    Function to gather the MD5 checksums of files from a local
    directory

    Parameters
    ----------
    base_dir : string
        filepath to the base directory where all of the files are
        located

    Returns
    -------
    md5_dict : dictionary {str : str}
        a dictionary where the key is the filepath and the value is
        the MD5 checksum of the file
    '''

    # Import packages
    import hashlib

    # Init variables
    fp_list = gather_files(base_dir)
    md5_dict = {}
    i = 0
    len_fp = len(fp_list)

    # Form a dictionary of md5 values from files on disk
    for fp in fp_list:
        f = open(fp, 'rb').read()
        md5_dict[fp] = hashlib.md5(f).hexdigest()
        i += 1
        print_loop_status(i, len_fp)

    # Return the dictionary
    return md5_dict


# Print status of file progression in loop
def print_loop_status(itr, full_len):
    '''
    Function to print the current percentage completed of a loop

    Parameters
    ----------
    itr : integer
        the current iteration of the loop
    full_len : integer
        the full length of the loop

    Returns
    -------
    None
        the function prints the loop status, but doesn't return a value
    '''

    # Print the percentage complete
    per = 100*(float(itr)/full_len)
    print '%d/%d\n%f%% complete' % (itr, full_len, per)

