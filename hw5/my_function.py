"""This file contains two function:
    get_data():to download data from url
    remove_data():to remove data from local address
"""

import os
import urllib3


def get_data(url):
    """This is a function to download data from url if provided url is valid
    parameters:
        url--character string of data file url address
    returns:
        if file already exists, then return None value
        if download successes, then return bool value True
        if url is not valid, then raise an exception
    """
    split_url = url.split('/')
    filename = split_url[len(split_url) - 1]
    # if file exists, return none
    if os.path.exists(filename):
        return None
    # if file does not exist, download from url
    else:
        # if url is valid,download file and return true
        try:
            http = urllib3.PoolManager()
            response = http.request('GET', url)
            with open(filename, 'wb') as file_name:
                file_name.write(response.data)
            return True
        # if url is not valid, raise exception
        except:
            raise ValueError("URL is not valid.")


def remove_data(filename):
    """This is a function to remove data file if the provided filename exists
    parameters:
        filename--character string, name of file to remove
    returns:
        if removing succeeds, then return bool value True
        if removing failed, then raise an exception
    """
    if os.path.exists(filename):
        os.remove(filename)
        return True
    else:
        raise ValueError("File does not exist.")
