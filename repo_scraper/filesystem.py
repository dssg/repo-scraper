#This file contains utility functions for working witht the filesytem

import os
import mimetypes as mime

def list_files_in(directory):
    '''Receives a path to a directory and returns
    paths to all files along with each mimetype'''
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_mimetypes(file_list):
    '''Returns a list of tuples (file, mimetype)'''
    files_and_mimetypes = [(f, mime.guess_type(f)[0]) for f in file_list]
    return files_and_mimetypes