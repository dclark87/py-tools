# CPAC/AWS/aws_utils.py
#
# Contributing authors:
# Daniel Clark

'''
This module contains functions which assist in interacting with AWS
services, including uploading/downloading data and file checking.
'''


# Get the MD5 sums of files on S3
def md5_sum(bucket, prefix='', filt_str=''):
    '''
    Function to get the filenames and MD5 checksums of files stored in
    an S3 bucket and return this as a dictionary.

    Parameters
    ----------
    bucket : boto.s3.bucket.Bucket instance
        an instance of the boto S3 bucket class to download from
    prefix : string (optional), default=''
        the bucket prefix where all of the file keys are located
    filt_str : string (optional), defualt=''
        a string to filter the filekeys of interest;
        e.g. 'matrix_data' will only return filekeys with the string
        'matrix_data' in their filepath name

    Returns
    -------
    md5_dict : dictionary {str : str}
        a dictionary where the keys are the S3 filename and the values
        are the MD5 checksum values
    '''

    # Import packages
    import file_utils

    # Init variables
    blist = bucket.list(prefix=prefix)
    md5_dict = {}
    i = 0
    no_files = len(blist)

    # And iterate over keys to copy over new ones
    for fkey in blist:
        filename = str(fkey.key)
        if filt_str in filename:
            md5_sum = str(fkey.etag).strip('"')
            md5_dict[filename] = md5_sum
            print 'filename: %s' % filename
            print 'md5_sum: %s' % md5_sum
        # Increment counter and update percentage complete
        i += 1
        file_utils.print_loop_status(i, no_files)

    # Return the dictionary
    return md5_dict


# Rename s3 keys from src_list to dst_list
def s3_rename(bucket, src_list, dst_list,
              keep_old=False, overwrite=False, make_public=False):
    '''
    Function to rename files from an AWS S3 bucket via a copy and delete
    process. Uses all keys in src_list as the original names and renames
    the them to the corresponding keys in the dst_list.
    (e.g. src_list[9] --> dst_list[9])

    Parameters
    ----------
    bucket : boto.s3.bucket.Bucket instance
        an instance of the boto S3 bucket class to download from
    src_list : list (str)
        a list of relative paths of the files to delete from the bucket
    dst_list : list (str)
        a list of relative paths of the files to delete from the bucket
    keep_old : boolean (optional), default=False
        flag indicating whether to keep the src_list files
    overwrite : boolean (optional), default=False
        flag indicated whether to overwrite the files in dst_list
    make_public : boolean (optional), default=False
        set to True if files should be publically available on S3
    Returns
    -------
    None
        The function doesn't return any value, it deletes data from
        S3 and prints its progress and a 'done' message upon completion
    '''

    # Check list lengths are equal
    if len(src_list) != len(dst_list):
        raise ValueError('src_list and dst_list are different lengths!')

    # Import packages
    import file_utils

    # Init variables
    i = 0
    no_files = len(src_list)

    # And iterate over keys to copy over new ones
    for f in src_list:
        src_key = bucket.get_key(f)
        if not src_key:
            print 'source file %s doesnt exist, skipping...' % f
            continue
        dst_key = dst_list[i]
        dst_exists = bucket.get_key(dst_key)
        if not dst_exists or overwrite:
            print 'copying source: ', str(src_key.key)
            print 'to destination: ', dst_key
            src_key.copy(bucket.name, dst_key)
            if make_public:
                print 'making public...'
                dk = bucket.get_key(dst_key)
                dk.make_public()
            if not keep_old:
                src_key.delete()
        else:
            print '%s exists and not overwriting' % dst_key
        # Increment counter and update percentage complete
        i += 1
        file_utils.print_loop_status(i, no_files)


# Delete s3 keys based on input list
def s3_delete(bucket, in_list):
    '''
    Method to delete files from an AWS S3 bucket that have the same
    names as those of an input list to a local directory.

    Parameters
    ----------
    bucket : boto.s3.bucket.Bucket instance
        an instance of the boto S3 bucket class to download from
    in_list : list (str)
        a list of relative paths of the files to delete from the bucket

    Returns
    -------
    None
        The function doesn't return any value, it deletes data from
        S3 and prints its progress and a 'done' message upon completion
    '''

    # Import packages
    import file_utils

    # Init variables
    no_files = len(in_list)
    i = 0

    # Iterate over list and delete S3 items
    for f in in_list:
        try:
            print 'attempting to delete %s from %s...' % (f, bucket.name)
            k = bucket.get_key(f)
            k.delete()
        except AttributeError:
            print 'No key found for %s on bucket %s' % (f, bucket.name)
        # Increment counter and update percentage complete
        i += 1
        file_utils.print_loop_status(i, no_files)


# Download files from AWS S3 to local machine
def s3_download(bucket, in_list, local_prefix, bucket_prefix=''):
    '''
    Method to download files from an AWS S3 bucket that have the same
    names as those of an input list to a local directory.

    Parameters
    ----------
    bucket : boto.s3.bucket.Bucket instance
        an instance of the boto S3 bucket class to download from
    in_list : list (str)
        a list of relative paths of the files to download from the bucket
    local_prefix : string
        local directory prefix to store the downloaded data
    bucket_prefix : string (optional)
        bucket_prefix, if specified, will be substituted with
        local_prefix; otherwise, the local_prefix will only prepend the
        downloaded files

    Returns
    -------
    None
        The function doesn't return any value, it downloads data from
        S3 and prints its progress and a 'done' message upon completion
    '''

    # Import packages
    import file_utils
    import os

    # Init variables
    no_files = len(in_list)
    i = 0

    # Check for trailing '/'
    if not local_prefix.endswith('/'):
        local_prefix = local_prefix + '/'
    if bucket_prefix and not bucket_prefix.endswith('/'):
        bucket_prefix = bucket_prefix + '/'

    # For each item in the list, try to download it
    for f in in_list:
        remote_filename = bucket.name + ': ' + f
        if bucket_prefix:
            local_filename = f.replace(bucket_prefix, local_prefix)
        else:
            local_filename = os.path.join(local_prefix, f)
        # Check to see if the local folder setup exists or not
        local_folders = os.path.dirname(local_filename)
        if not os.path.isdir(local_folders):
            print 'creating %s on local machine' % local_folders
            os.makedirs(local_folders)
        # Attempt to download the file
        print 'attempting to download %s to %s...' \
            % (remote_filename, local_filename)
        try:
            if not os.path.exists(local_filename):
                k = bucket.get_key(f)
                k.get_contents_to_filename(local_filename)
            else:
                print 'File %s already exists, skipping...' % local_filename
        except AttributeError:
            print 'No key found for %s on bucket %s' % (f, bucket.name)
        # Increment counter and update percentage complete
        i += 1
        file_utils.print_loop_status(i, no_files)

    # Done iterating through list
    print 'done!'


# Upload files to AWS S3
def s3_upload(bucket, src_list, dst_list, make_public=False, overwrite=False):
    '''
    Function to upload a list of data to an S3 bucket

    Parameters
    ----------
    bucket : boto.s3.bucket.Bucket instance
        an instance of the boto S3 bucket class to download from
    src_list : list (str)
        list of filepaths as strings to upload to S3
    dst_list : list (str)
        list of filepaths as strings coinciding with src_list, such
        that src_list[1] gets uploaded to S3 with the S3 path given in
        dst_list[1]
    make_public : boolean (optional), default=False
        set to True if files should be publically available on S3
    overwrite : boolean (optional), default=False
        set to True if the uploaded files should overwrite what is
        already there

    Returns
    -------
    None
        The function doesn't return any value, it uploads data to S3
        and prints its progress and a 'done' message upon completion
    '''

    # Callback function for upload progress update
    def callback(complete, total):
        '''
        Method to illustrate file uploading and progress updates
        '''

        # Import packages
        import sys

        # Write ...'s to the output for loading progress
        sys.stdout.write('.')
        sys.stdout.flush()

    # Import packages
    import file_utils

    # Init variables
    no_files = len(src_list)
    i = 0

    # Check if the list lengths match 
    if no_files != len(dst_list):
        raise RuntimeError, 'src_list and dst_list must be the same length!'

    # For each source file, upload
    for src_file in src_list:
        # Get destination path
        dst_file = dst_list[i]
        # Print status
        print 'Uploading %s to S3 bucket %s as %s' % \
        (src_file, bucket.name, dst_file)

        # Create a new key from the bucket and set its contents
        k = bucket.new_key(dst_file)
        if k.exists() and not overwrite:
            print 'key %s already exists, skipping...' % dst_file
        else:
            k.set_contents_from_filename(src_file, cb=callback, replace=True)
        # Make file public if set to True
        if make_public:
            print 'make public()'
            k.make_public()
        # Increment counter and update percentage complete
        i += 1
        file_utils.print_loop_status(i, no_files)

    # Print when finished
    print 'Done!'
